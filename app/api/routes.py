from fastapi import APIRouter
from app.models.schemas import ProjectRequest
from app.agents.orchestrator import AutoDevOrchestrator

router = APIRouter()

@router.post("/generate")
async def generate_project(request: ProjectRequest):
    orchestrator = AutoDevOrchestrator()
    result = await orchestrator.run(request.description)
    return {"result": result}
