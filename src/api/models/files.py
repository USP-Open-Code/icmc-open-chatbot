from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from src.infrastructure.config import settings


class FileMetadata(BaseModel):
    metadata: Optional[Dict[str, Any]] = Field(default={
        "created_at": datetime.now().isoformat(),
        "collection_name": settings.INDEX_NAME
    })
