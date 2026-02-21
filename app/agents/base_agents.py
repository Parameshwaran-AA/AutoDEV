from abc import ABC, abstractmethod
from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class BaseAgent(ABC):

    def __init__(self, role: str):
        self.role = role

    async def llm_call(self, prompt: str):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": self.role},
                      {"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    @abstractmethod
    async def execute(self, input_data: str):
        pass
