from google.adk.agents import Agent
from .tools import get_tools


math_agent = Agent(
    name="math_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to Mathematics."),
    instruction=(
        "You are a helpful agent who can answer user questions related to Mathematics."
    ),
    tools=get_tools(),
)
