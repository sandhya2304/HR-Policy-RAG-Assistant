"""Step 7 Build the agent that ties the LLM and search the tool together"""


from langchain.agents import create_agent
from hr_assistant import config

def create_hr_agent(llm,search_tool):
    """Return an agent that can answer questions about 
    the HR Policy document."""
    return create_agent(
        llm=llm,
        tools=[search_tool],
        system_prompt=config.SYSTEM_PROMPT,
        verbose=True
    )