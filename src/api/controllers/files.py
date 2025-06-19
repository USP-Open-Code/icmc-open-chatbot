from src.services.document_reader import DocumentReader
from src.infrastructure.database import ChromaDB
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.infrastructure.config import settings
from src.api.models import FileMetadata

from fastapi import UploadFile


async def controller_upload_file(
    file: UploadFile,
    metadata: FileMetadata,
    vector_store: ChromaDB
):
    try:
        content = await DocumentReader.read_file(file)
        metadata = metadata.model_dump()["metadata"]
        metadata["extension"] = content["extension"]
        metadata["file_name"] = content["name"]

        langchain_docs = []

        for j, text_content in enumerate(content["content"]):
                    doc = Document(
                        page_content=text_content,
                        metadata={
                            'extension' : content["extension"],
                            'file_name' : content["name"]

                            }
                    )
                    langchain_docs.append(doc)
        await vector_store.add_documents(
            documents=langchain_docs
        )
        return True
    except Exception as e:
        raise ValueError(f"Error uploading file: {e}")


async def controller_list_collections(
    vector_store: ChromaDB
):
    return await vector_store.list_collections()


async def controller_list_files(
    collection_name: str,
    vector_store: ChromaDB
):
    return await vector_store.list_documents(collection_name)


async def controller_delete_file(
    collection_name: str,
    file_id: str,
    vector_store: ChromaDB
):
    return await vector_store.delete_documents(
        ids=[file_id],
        collection_name=collection_name
    )
