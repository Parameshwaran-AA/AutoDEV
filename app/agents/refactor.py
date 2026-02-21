from app.agents.base_agents import BaseAgent
from app.tools.lint_tool import LintTool


class RefactorAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "You are a senior engineer improving performance, readability, and scalability."
        )
        self.lint_tool = LintTool()

    async def execute(self, code: str):
        improved = await self.llm_call(
            f"Refactor and optimize this production code:\n{code}"
        )

        lint_result = self.lint_tool.run_linter()

        return {"refactored_code": improved, "lint": lint_result}
