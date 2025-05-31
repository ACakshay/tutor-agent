import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from .math_agent import math_agent


root_agent = Agent(
    name="tutor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions academic questions about physics, and mathematics"
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about physics, and mathematics"
    ),
    sub_agents=[math_agent],
)
