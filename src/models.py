from pydantic import BaseModel
from typing import List, Optional

class ScopeConfig(BaseModel):
    domains: List[str]
    ip_ranges: List[str]

class Task(BaseModel):
    id: str
    description: str
    command: str
    status: str = "pending"
    output: Optional[str] = None

class PipelineState(BaseModel):
    tasks: List[Task]
    scope: ScopeConfig
    logs: List[str]