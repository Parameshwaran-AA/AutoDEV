from app.agents.base_agents import BaseAgent
from app.tools.file_tool import FileTool


class DebuggerAgent(BaseAgent):

    def __init__(self):
        super().__init__("You are a debugging expert fixing Python errors.")
        self.file_tool = FileTool()

    async def execute(self, error_output: str):
        fix = await self.llm_call(
            f"Fix the following error and return corrected code:\n{error_output}"
        )

        self.file_tool.write_file("workspace/generated.py", fix)
        return fix
