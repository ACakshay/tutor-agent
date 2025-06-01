from google.adk.agents import Agent
from .tools import get_tools


math_agent = Agent(
    name="math_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions related to Mathematics."),
    instruction=(
        "you are a mathematician and  a helpful agent who can answer user questions related to Mathematics. Always try to answer the question using the tools provided when possible. If you are unable to answer the question then transfer it to relevant agent"
    ),
    tools=get_tools(),
)
