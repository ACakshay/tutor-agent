from google.adk.agents import Agent
from .tools import get_tools


chemistry_agent = Agent(
    name="chemistry_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to Chemistry."),
    instruction=(
        "You are a helpful agent who can answer user questions related to Chemistry."
    ),
    tools=get_tools(),
)
