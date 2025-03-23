from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from src.infrastructure.config import settings


class FileMetadata(BaseModel):
    collection_name: str = Field(default=settings.INDEX_NAME)
    metadatas: Optional[Dict[str, Any]] = None
