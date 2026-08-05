from pydantic import BaseModel
from typing import Optional, Dict, Any

class RequestModel(BaseModel):
    query: str
    top_k: Optional[int] = 5
    metadata: Optional[Dict[str, Any]] = None
