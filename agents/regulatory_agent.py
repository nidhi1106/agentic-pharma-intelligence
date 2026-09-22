import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

def regulatory_agent(state):

    response = llm.invoke(
        f"""
        You are Regulatory Affairs Agent.

        Query:
        {state['query']}

        Find:

        FDA actions
        EMA actions
        Label changes
        Safety alerts
        """
    )

    state["regulatory_findings"] = response.content

    return state