from agno.agent import Agent

from src.config.prompts import AGENT_INSTRUCTION
from src.agents import gpt
from src.models.pydantic_models import Answer
from src.tools import TOOLS, zoom_tools

sentivisor = Agent(
	name="sentivisor",
	model=gpt,
	instructions=AGENT_INSTRUCTION,
	# response_model=Answer, # optional for structured outputs or api response
    tools=TOOLS['sentivisor']+zoom_tools,
    structured_outputs=False,
    stream=True
)