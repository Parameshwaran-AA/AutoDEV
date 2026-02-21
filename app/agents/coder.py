from app.agents.base_agents import BaseAgent
from app.tools.file_tool import FileTool


class CoderAgent(BaseAgent):

    def __init__(self):
        super().__init__("You are a production-grade Python engineer.")
        self.file_tool = FileTool()

    async def execute(self, input_data: str):
        code = await self.llm_call(f"Write production-ready Python code:\n{input_data}")
        self.file_tool.write_file("workspace/generated.py", code)
        return code
