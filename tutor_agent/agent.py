import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from .math_agent import math_agent
from .physics_agent import physics_agent
from .chemistry_agent import chemistry_agent


root_agent = Agent(
    name="tutor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions academic questions about physics, and mathematics"
    ),
    instruction=(
        "You are a helpful agent who uses the relevant subagent to answer user questions about physics, mathematics and mathematics. For any quuestion outside of these domains, you should respond with 'I can not help with this question, Please ask question related to Maths,physics or chemistry'. "
    ),
    sub_agents=[math_agent, physics_agent, chemistry_agent],
)
