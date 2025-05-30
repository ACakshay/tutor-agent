from google.adk.agents import Agent
from physics_agent.tools import get_tools


physics_agent = Agent(
    name="physics_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to physics."),
    instruction=(
        "You are a helpful agent who can answer user questions related to physics."
    ),
    tools=get_tools(),
)
