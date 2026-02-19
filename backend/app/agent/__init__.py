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
from netra import Netra, ConversationType
from langgraph.runtime import Runtime

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
    middleware=[netra_conversation_middleware, ModelRetryMiddleware(
        max_delay=2,
        max_retries=5
    )]
)

@agent(name="Nova")
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



    return response["messages"][-1].text