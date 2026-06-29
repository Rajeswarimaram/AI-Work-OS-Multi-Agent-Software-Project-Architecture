import json
import os
from datetime import datetime

MEMORY_FOLDER = "memory"
MEMORY_FILE = os.path.join(
    MEMORY_FOLDER,
    "history.json"
)
def save_history(
    project_name: str,
    task_type: str,
    confidence_score: int
) -> None:
    """
    Saves the completed project
    into the project history.
    """

    os.makedirs(
        MEMORY_FOLDER,
        exist_ok=True
    )

    project_history = []

    if os.path.exists(MEMORY_FILE):

        try:

            with open(
                MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as history_file:

                project_history = json.load(
                    history_file
                )

        except Exception:

            project_history = []

    project_history.append({

        "project_name": project_name,

        "task_type": task_type,

        "confidence_score": confidence_score,

        "status": "Completed",

        "generated_by": "AI WorkOS",

        "version": "1.0",

        "created_at": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    })

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as history_file:

        json.dump(
            project_history,
            history_file,
            indent=4,
            ensure_ascii=False
        )
def load_history() -> list:
    """Loads all previously
    completed projects."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as history_file:

            return json.load(
                history_file
            )
    except Exception:
        return []

def get_last_project() -> dict | None:
    """Returns the most recently
    completed project."""
    project_history = load_history()
    if project_history:
        return project_history[-1]
    return None

def get_total_projects() -> int:
    """Returns the total number
    of completed projects."""
    project_history = load_history()
    return len(project_history)