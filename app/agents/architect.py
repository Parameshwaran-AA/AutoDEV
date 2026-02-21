from app.agents.base_agents import BaseAgent


class ArchitectAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "You are a senior software architect. "
            "Design scalable architecture with modules, patterns, and best practices."
        )

    async def execute(self, input_data: str):
        prompt = f"""
        Based on the plan below, design a scalable Python project architecture.
        Include:
        - Modules
        - Design patterns
        - Folder structure
        - Key interfaces

        Plan:
        {input_data}
        """
        return await self.llm_call(prompt)
