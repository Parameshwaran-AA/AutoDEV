from app.agents.planner import PlannerAgent
from app.agents.architect import ArchitectAgent
from app.agents.coder import CoderAgent
from app.agents.tester import TesterAgent
from app.agents.debugger import DebuggerAgent
from app.agents.refactor import RefactorAgent


class AutoDevOrchestrator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.architect = ArchitectAgent()
        self.coder = CoderAgent()
        self.tester = TesterAgent()
        self.debugger = DebuggerAgent()
        self.refactor = RefactorAgent()

    async def run(self, requirement: str):

        plan = await self.planner.execute(requirement)

        architecture = await self.architect.execute(plan)

        code = await self.coder.execute(architecture)

        test_output = await self.tester.execute(code)

        if "failed" in test_output["results"].lower():
            fixed_code = await self.debugger.execute(test_output["results"])
            code = fixed_code

        refactored = await self.refactor.execute(code)

        return {
            "plan": plan,
            "architecture": architecture,
            "code": code,
            "tests": test_output,
            "refactor": refactored
        }
