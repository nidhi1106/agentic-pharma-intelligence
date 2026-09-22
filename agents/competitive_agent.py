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

def competitive_agent(state):

    response = llm.invoke(
        f"""
        You are Competitive Intelligence Agent.

        Query:
        {state['query']}

        Analyze:

        Competitors
        Acquisitions
        Partnerships
        Market shifts
        """
    )

    state["competitive_findings"] = response.content

    return state