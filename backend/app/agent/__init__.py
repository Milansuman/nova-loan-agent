from langchain.agents import create_agent
from langchain.agents.middleware import after_agent, AgentState, ModelResponse, ModelRetryMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from agent.llm import llm
from agent.prompt import SYSTEM_PROMPT
from agent.tools import (
    verify_identity,
    calculate_emi,
    check_eligibility,
    fetch_credit_report,
    fetch_financial_profile,
    generate_pre_approval,
    search_loan_products
)
from netra.decorators import agent
from netra import Netra, ConversationType, SpanType, UsageModel
from langgraph.runtime import Runtime
from langchain.messages import AnyMessage

@after_agent
def netra_conversation_middleware(state: AgentState, runtime: Runtime):
    Netra.add_conversation(
        conversation_type=ConversationType.INPUT,
        content=SYSTEM_PROMPT,
        role="System"
    )

    for message in state["messages"]:
        if message.type == "human":
            Netra.add_conversation(
                conversation_type=ConversationType.INPUT,
                content=message.text,
                role="User"
            )
        elif message.type == "ai":
            Netra.add_conversation(
                conversation_type=ConversationType.OUTPUT,
                content=message.text,
                role="Ai"
            )

            for tool_call in message.tool_calls:
                Netra.add_conversation(
                    conversation_type=ConversationType.INPUT,
                    content=f"""{tool_call["name"]}({tool_call["args"]})""",
                    role="Tool Call"
                )
        elif message.type == "tool":
            Netra.add_conversation(
                conversation_type=ConversationType.OUTPUT,
                content=message.content,
                role="Tool Output"
            )

_agent = create_agent(
    model=llm,
    system_prompt=SYSTEM_PROMPT,
    tools=[
        verify_identity,
        calculate_emi,
        check_eligibility,
        fetch_credit_report,
        fetch_financial_profile,
        generate_pre_approval,
        search_loan_products
    ],
    checkpointer=InMemorySaver(),
    middleware=[
        # netra_conversation_middleware, 
        ModelRetryMiddleware(
            max_delay=2,
            max_retries=5
        )
    ]
)

# @agent(name="Nova")
def get_response(prompt: str, thread_id: str):
    response = _agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }, {
        "configurable": {
            "thread_id": thread_id
        }
    })

    trace_conversation(thread_id)
    return response["messages"][-1].text

def trace_conversation(thread_id: str):
    messages: list[AnyMessage] = _agent.get_state({
        "configurable": {
            "thread_id": thread_id
        }
    }).values["messages"]

    with Netra.start_span("Nova", as_type=SpanType.AGENT) as agent_span:
        Netra.set_session_id(thread_id)
        Netra.set_user_id("Demo")
        Netra.set_tenant_id("Nova")

        tool_calls = {}

        for message in messages:
            if message.type == "human":
                Netra.add_conversation(
                    conversation_type=ConversationType.INPUT,
                    content=message.text,
                    role="User"
                )
            elif message.type == "ai":

                if len(message.text) > 0:
                    with Netra.start_span("Agent Response", as_type=SpanType.GENERATION) as response_span:
                        response_span.set_model("gpt-4.1")

                        input_usage = UsageModel(
                            model="gpt-4.1",
                            units_used=message.usage_metadata["input_tokens"] if message.usage_metadata else 0,
                            usage_type="input"
                        )

                        output_usage = UsageModel(
                            model="gpt-4.1",
                            units_used=message.usage_metadata["output_tokens"] if message.usage_metadata else 0,
                            usage_type="output"
                        )

                        response_span.set_usage([input_usage, output_usage])
                        response_span.set_attribute("completion", message.text)

                        Netra.add_conversation(
                            conversation_type=ConversationType.OUTPUT,
                            content=message.text,
                            role="Ai"
                        )
                        
                for tool_call in message.tool_calls:
                    tool_calls[tool_call["id"]] = {
                        "name": tool_call["name"],
                        "args": tool_call["args"]
                    }

                    Netra.add_conversation(
                        conversation_type=ConversationType.INPUT,
                        content=f"""{tool_call["name"]}({tool_call["args"]})""",
                        role="Tool Call"
                    )
            elif message.type == "tool":
                tool_calls[message.tool_call_id]["output"] = message.content

                with Netra.start_span(tool_calls[message.tool_call_id]["name"], as_type=SpanType.TOOL) as tool_span:
                    tool_span.set_attribute("tool.name", tool_calls[message.tool_call_id]["name"])
                    tool_span.set_attribute("tool.args", str(tool_calls[message.tool_call_id]["args"]))
                    tool_span.set_attribute("tool.output", str(message.content))

                Netra.add_conversation(
                    conversation_type=ConversationType.OUTPUT,
                    content=message.content,
                    role="Tool Output"
                )
            elif message.type == "system":
                Netra.add_conversation(
                    conversation_type=ConversationType.INPUT,
                    content=SYSTEM_PROMPT,
                    role="System"
                )