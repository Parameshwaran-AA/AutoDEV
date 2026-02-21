from pydantic import BaseModel

class ProjectRequest(BaseModel):
    description: str
