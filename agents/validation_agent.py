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

def validation_agent(state):

    response = llm.invoke(
        f"""
        Validate findings.

        Clinical:
        {state['clinical_findings']}

        Regulatory:
        {state['regulatory_findings']}

        Competitive:
        {state['competitive_findings']}

        Check:

        - confidence
        - consistency
        - factual alignment
        """
    )

    state["validation_result"] = response.content

    return state