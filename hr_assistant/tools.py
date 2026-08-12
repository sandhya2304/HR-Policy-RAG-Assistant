"""Step 5 wrap the retreiver as a tool the agent can call"""

from langchain.tools import tool

def create_search_tool(retriever):
    """return a @tool function that searches the HR Policy document"""


    @tool
    def search_hr_policy(query: str) -> str:
     """Search the HR Policy document for relevant information."""
    results = retriever.invoke(query)
    return "\n".join(chunk.page_content for chunk in results)

 return search_hr_policy