from agents.research_agent import research_agent
from agents.execution_agent import execution_agent
from agents.testing_agent import testing_agent
from agents.critic_agent import critic_agent
from agents.synthesizer_agent import synthesizer_agent
from agents.memory_agent import save_history
from reports.report_generator import generate_report
from utils.logger import log


def orchestrator_agent(user_request: str) -> dict:

    """Controls the complete AI WorkOS workflow by
    coordinating all AI agents from research
    to report generation."""

    log("Project Started")
    task_type = "Software Engineering"
    log("Research Agent Started")
    research_output = research_agent(user_request)
    log("Research Agent Completed")
    log("Execution Agent Started")
    execution_output = execution_agent(
        task_type,
        research_output
    )
    log("Execution Agent Completed")
    log("Testing Agent Started")
    testing_output = testing_agent(
        task_type,
        execution_output
    )
    log("Testing Agent Completed")

    log("Critic Agent Started")
    critic_output = critic_agent(
        research_output,
        execution_output,
        testing_output
    )
    log("Critic Agent Completed")

    log("Synthesizer Agent Started")
    final_report = synthesizer_agent(
        user_request,
        task_type,
        research_output,
        execution_output,
        testing_output,
        critic_output
    )
    log("Synthesizer Agent Completed")

    log("Saving Project History")

    save_history(
        user_request,
        task_type,
        final_report["confidence"]["score"]
    )
    log("Project History Saved")
    log("Generating Reports")
    generate_report(final_report)
    log("Reports Generated Successfully")
    log("Project Completed")
    return final_report