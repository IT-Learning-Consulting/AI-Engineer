"""
Handles the logging of all user interactions with the app.

This module records user actions and system events in a log file with timestamps,
enabling tracking, debugging, and analysis of user behavior and system usage.
Currently logs are stored locally, with plans for cloud support in the future.

Functions:
- log_action: Logs a user or system action with a timestamp and category.
- reset_log: Clears all existing logs, typically when starting a new session.
"""

import os
from datetime import datetime
from global_settings import LOG_FILE


def log_action(action: str, action_type: str) -> None:
    """
    Records a user or system action in the log file with a timestamp.

    This function appends a formatted log entry to the LOG_FILE, capturing
    when the action occurred and categorizing it for better tracking.

    Args:
        action (str): A description of what occurred.
        action_type (str): The category or type of action (e.g., 'USER', 'SYSTEM').
    """
    # Generate a timestamp for the log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log entry string
    log_entry = f"{timestamp}: {action_type} : {action}\n"

    # Append the log entry to the log file
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_entry)


def reset_log() -> None:
    """
    Clears all contents of the log file.

    This function truncates the log file, removing all existing entries.
    Typically used when starting a new session to keep the log concise.
    Not recommended for production environments where historical logs are important.
    """
    # Open the log file in write mode and clear its contents
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        file.truncate(0)
