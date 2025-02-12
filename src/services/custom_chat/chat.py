from src.infrastructure.config import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import BaseTool
from typing import List


class CustomChat:
    def __init__(self, model: LLM, sys_prompt: str):
        self.model = model
        self.sys_prompt = sys_prompt
        self._prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.sys_prompt),
            ("user", "{input}")
        ])

    async def __call__(self, user_input: str):
        # TO DO: add bind_tools
        self.chain = self._prompt_template | self.model
        response = self.chain.invoke({"input": user_input})
        return response

    def add_tools(self, tools: List[BaseTool]):
        pass
