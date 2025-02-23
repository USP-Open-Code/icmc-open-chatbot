from pydantic import BaseModel
from typing import Optional, Dict, Any


class FileMetadata(BaseModel):
    collection_name: str
    metadatas: Optional[Dict[str, Any]] = None
