from langchain.agents import create_agent
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
    checkpointer=InMemorySaver()
)

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