from google.adk.agents import Agent

from tutor_agent.math_agent import math_agent
from tutor_agent.chemistry_agent import chemistry_agent

from tutor_agent.physics_agent import physics_agent


root_agent = Agent(
    name="tutor_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions academic questions about Physics, Mathematics and Chemistry"
    ),
    instruction=(
        """You are a very smart helpful agent who always uses the relevant sub-agent to answer user questions if it's about physics, mathematics and mathematics. NEVER ANSWER YOURSELF, ALWAYS USE THE RELEVANT SUB-AGENT TO ANSWER THE QUESTION. 
        For any questions which are surely outside of academics and not related to any of the mentioned subject and you are sure that it's not of your capabilities, you should respond that you can't help and tell why you can't help. always try to use sub-agents to answer the question if it's related to any of the subjects mentioned above. if you need to search Internet transfer request to  chemistry_agent.
        Make sure that only reject the query if it's not even remotely related to the subjects, otherwise you should try to answer it using the relevant subagent.
        Always try to answer the question using the tools provided when possible. If you are unable to answer the question then transfer it to relevant agent."""
    ),
    global_instruction="Always try to answer the question using the tools provided when possible. If you are unable to answer the question then transfer it to relevant agent.ALways verify your answer with helping tools before responding to the user. Don't relay on your own knowledge, use the tools provided to verify your answer. and never assume anything.",
    sub_agents=[math_agent, chemistry_agent, physics_agent],
)
