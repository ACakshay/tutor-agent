from google.adk.agents import Agent
from .tools import get_tools


physics_agent = Agent(
    name="physics_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to physics."),
    instruction=(
        "you are a physicist and a helpful agent who can answer user questions related to physics.Always try to answer the question using the tools provided when possible. If you are unable to answer the question then transfer it to relevant agent"
    ),
    tools=get_tools(),
)
