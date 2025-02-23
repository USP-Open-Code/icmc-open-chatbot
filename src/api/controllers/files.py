from fastapi import UploadFile

from src.services.document_reader import DocumentReader
from src.infrastructure.database import ChromaDB
from src.api.models import FileMetadata


async def controller_upload_file(
    metadata: FileMetadata,
    file: UploadFile,
    vector_store: ChromaDB
):
    try:
        content = await DocumentReader.read_file(file)
        await vector_store.add_documents(
            documents=[content["content"]],
            collection_name=metadata.collection_name,
            metadatas=[metadata.metadatas] if metadata.metadatas else None,
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
