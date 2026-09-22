import os

from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment=os.getenv("AZURE_EMBEDDING_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)