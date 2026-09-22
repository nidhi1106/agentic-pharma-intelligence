from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

from vectorstore.embeddings import embeddings

def create_vector_store():

    docs = [

        Document(
            page_content="FDA approved Drug X for NSCLC"
        ),

        Document(
            page_content="Phase III trial achieved primary endpoint"
        ),

        Document(
            page_content="Competitor acquired oncology startup"
        )

    ]

    db = FAISS.from_documents(
        docs,
        embeddings
    )

    db.save_local("faiss_db")

def get_retriever():

    db = FAISS.load_local(
        "faiss_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever(
        search_kwargs={"k":5}
    )