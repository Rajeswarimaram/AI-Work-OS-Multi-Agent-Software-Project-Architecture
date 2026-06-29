from prompts.critic_prompt import CRITIC_PROMPT
from services.llm_service import generate_response
from utils.json_parser import parse_json


def critic_agent(
    research_output: str,
    execution_output: str,
    testing_output: dict
) -> dict:
    """Performs a detailed software review
    and provides project improvement suggestions."""

    final_prompt = CRITIC_PROMPT.format(
        research_output=research_output,
        execution_output=execution_output,
        testing_output=testing_output
    )

    project_review = generate_response(final_prompt)

    print("\n========== CRITIC AGENT RAW OUTPUT ==========\n")
    print(project_review)
    print("\n=============================================\n")

    return parse_json(project_review)