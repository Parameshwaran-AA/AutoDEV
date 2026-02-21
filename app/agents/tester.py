from app.agents.base_agents import BaseAgent
from app.tools.file_tool import FileTool
from app.tools.test_tool import TestTool


class TesterAgent(BaseAgent):

    def __init__(self):
        super().__init__("You are an expert QA engineer writing pytest tests.")
        self.file_tool = FileTool()
        self.test_tool = TestTool()

    async def execute(self, code: str):
        tests = await self.llm_call(
            f"Write pytest test cases for this code:\n{code}"
        )

        self.file_tool.write_file("workspace/test_generated.py", tests)

        results = self.test_tool.run_tests()

        return {"tests": tests, "results": results}
