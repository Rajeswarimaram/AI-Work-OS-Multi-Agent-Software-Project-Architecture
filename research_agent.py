from prompts.research_prompt import RESEARCH_PROMPT
from services.llm_service import generate_response

def research_agent(user_request: str) -> str:
    """Performs requirement analysis for the given
    software project and prepares a research report."""
    formatted_prompt = RESEARCH_PROMPT.format(
        user_request=user_request
    )
    project_research = generate_response(formatted_prompt)
    return project_research