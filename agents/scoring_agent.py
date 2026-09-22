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

def scoring_agent(state):

    response = llm.invoke(
        f"""
        Calculate:

        Clinical Risk Score
        Regulatory Risk Score
        Competitive Threat Score

        Findings:

        {state['clinical_findings']}
        {state['regulatory_findings']}
        {state['competitive_findings']}

        Return JSON.
        """
    )

    state["impact_score"] = response.content

    return state