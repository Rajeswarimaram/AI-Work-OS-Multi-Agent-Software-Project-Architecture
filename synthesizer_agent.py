from datetime import datetime
from utils.confidence_score import calculate_confidence

def synthesizer_agent(
    user_request: str,
    task_type: str,
    research_output: str,
    execution_output: str,
    testing_output: dict,
    critic_output: dict
)-> dict:
    
    """Combines all agent outputs into
    a single project report."""
    confidence_result = calculate_confidence(
        testing_output,
        critic_output
    )
    complete_report = {
        "project": user_request,
        "task_type": task_type,
        "generated_at": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        ),

        "status": "Completed",

        "research_report": research_output,

        "implementation_report": execution_output,

        "testing_report": testing_output,

        "review_report": critic_output,

        "confidence": confidence_result,

        "summary": {

            "overall_status": testing_output.get(
                "status",
                "Unknown"
            ),

            "quality_score": testing_output.get(
                "quality_score",
                0
            ),

            "deployment_ready": critic_output.get(
                "deployment_ready",
                False
            ),

            "industry_rating": critic_output.get(
                "industry_rating",
                "Unknown"
            )
        },

        "future_scope": [

            "Implement user authentication",

            "Support cloud deployment",

            "Integrate multiple AI models",

            "Enable project collaboration",

            "Add analytics dashboard",

            "Provide real-time monitoring"
        ]
    }
    return complete_report