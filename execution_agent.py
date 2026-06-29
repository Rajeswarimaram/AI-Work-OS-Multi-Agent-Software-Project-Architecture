from prompts.execution_prompt import EXECUTION_PROMPT
from services.llm_service import generate_response

def execution_agent(task_type: str, research_output: str) -> str:
    """Creates a detailed implementation plan
    based on the research analysis."""
    final_prompt = EXECUTION_PROMPT.format(
        research_output=research_output
    )
    implementation_report = generate_response(final_prompt)
    return implementation_report