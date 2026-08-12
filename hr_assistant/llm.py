"""Step 6 Connect to the LLM (the brain of the agent)"""


from langchain_groq import ChatGroq
from hr_assistant import config

def get_llm():
    """Return a Groq chat model. Read GROQ_API_KEY from the environment."""
    return ChatGroq(model_name=config.LLM_MODEL_NAME, 
                    temperature = 0)