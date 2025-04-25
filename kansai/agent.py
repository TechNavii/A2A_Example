from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

kansai_agent = Agent(
    name="kansai_agent",
    model=LiteLlm(model="gemini/gemini-2.5-flash-preview-04-17"),
    description="Talks in Kansa Dialect in Japanese",
    instruction="You are a japanese wo lives in kansai area. You will act as a japanese person in kansai dialect."
)