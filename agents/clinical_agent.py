import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

from vectorstore.faiss_store import get_retriever

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

def clinical_agent(state):

    retriever = get_retriever()

    docs = retriever.invoke(state["query"])

    context = "\n".join(
        [d.page_content for d in docs]
    )

    response = llm.invoke(
        f"""
        You are a Clinical Intelligence Agent.

        Query:
        {state['query']}

        Context:
        {context}

        Analyze:

        - Clinical trials
        - Safety signals
        - Endpoints
        - Biomarkers
        """
    )

    state["clinical_findings"] = response.content

    return state