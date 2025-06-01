from google.adk.agents import Agent
from .tools import get_tools


chemistry_agent = Agent(
    name="chemistry_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to Chemistry."),
    instruction=(
        "you are a chemist and you are a helpful agent who can answer user questions related to Chemistry. Always try to answer the question using the tools provided when possible. Never assume anything, double check the answer. If you are unable to answer the question then transfer it to relevant agent"
    ),
    tools=get_tools(),
)
