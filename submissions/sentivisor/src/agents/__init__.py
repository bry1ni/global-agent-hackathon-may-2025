from agno.models.openai import OpenAIChat

gpt = OpenAIChat(
	id="gpt-4o", # for multimodal input
	temperature=0.4,
)

AGENT_RESPONSE_KEYS = {
    "sentivisor": ["answer"],
}
