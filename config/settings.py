from dotenv import load_dotenv
import os

load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

if not AZURE_STORAGE_CONNECTION_STRING:
    raise ValueError(
        "AZURE_STORAGE_CONNECTION_STRING not found in .env"
    )

BLOB_CONTAINER = os.getenv("BLOB_CONTAINER")

if not BLOB_CONTAINER:
    raise ValueError(
        "BLOB_CONTAINER not found in .env"
    )

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in .env"
    )