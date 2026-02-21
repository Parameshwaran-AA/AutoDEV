from app.agents.base_agents import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("You are a senior software planner.")

    async def execute(self, input_data: str):
        prompt = f"Break this requirement into implementation steps:\n{input_data}"
        return await self.llm_call(prompt)
