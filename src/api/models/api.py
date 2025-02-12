from typing import Optional
from pydantic import BaseModel


class APIResponse(BaseModel):
    status_code: int
    status_message: Optional[str] = None
    response: Optional[dict] = None


class APIRequest(BaseModel):
    message: str
    user_id: str
    service_name: Optional[str] = None
