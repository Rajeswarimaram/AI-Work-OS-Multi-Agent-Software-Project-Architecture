import os
from datetime import datetime

LOG_FOLDER = "logs"

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "system.log"
)
def log(log_message: str) -> None:
    """Records application events
    into the system log file."""
    os.makedirs(
        LOG_FOLDER,
        exist_ok=True
    )
    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )
    formatted_log = (
        f"[{current_time}] {log_message}"
    )
    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(
            formatted_log + "\n"
        )
    print(formatted_log)