"""
Handles storing and retrieving session information locally,
with future support planned for cloud-based storage.

This module provides three core functions:
- save_session: Writes the current session state to a local YAML file.
- load_session: Reads the session state from a YAML file and updates the provided dictionary.
- delete_session: Removes the session file and clears the in-memory session state.
"""

import os
from typing import Dict, Any
import yaml
from global_settings import SESSION_FILE


def save_session(state):
    """
    Saves the current session state to a YAML file.

    This function takes a dictionary representing the current session state and writes
    it to a file specified by the constant SESSION_FILE in YAML format. This allows
    the session to be easily restored later.

    Args:
        state (Dict[str, Any]): A dictionary containing the current session's state.
    """

    # Create a copy of the state dictionary to ensure the original is not altered
    state_to_save = dict(state.items())

    # Open the session file in write mode and dump the state as YAML
    with open(SESSION_FILE, "w", encoding="utf-8") as file:
        yaml.dump(
            state_to_save,
            file,
        )


def load_session(state: Dict[str, Any]) -> bool:
    """
    Loads the session state from a YAML file into the provided state dictionary.

    This function checks whether the session file defined by SESSION_FILE exists.
    If it does, the file is read and parsed using YAML. The parsed data is then
    merged into the provided state dictionary. Returns True if loading is successful,
    otherwise returns False.

    Args:
        state (Dict[str, Any]): The dictionary to be updated with the loaded session state.

    Returns:
        bool: True if the session was successfully loaded and parsed, False otherwise.
    """
    # Check if the session file exists
    if os.path.exists(SESSION_FILE):
        # Open and attempt to read the file
        with open(SESSION_FILE, "r", encoding="utf-8") as file:
            # Load YAML data safely and default to an empty dict if None
            try:
                loaded_state = yaml.safe_load(file) or {}
                # Update the provided state dictionary with loaded values
                for key, value in loaded_state.items():
                    state[key] = value
                return True
            except yaml.YAMLError:
                # Return False if YAML parsing fails
                return False
    # Return False if the session file does not exist
    return False


def delete_session(state: Dict[str, Any]) -> None:
    """
    Deletes the session file and clears the current session state.

    This function removes the session file defined by SESSION_FILE if it exists,
    and then clears all keys from the provided state dictionary to reset the session.

    Args:
        state (Dict[str, Any]): The dictionary representing the current session state,
                                which will be cleared.
    """
    # Remove the session file if it exists
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

    # Clear all keys from the state dictionary
    for key in list(state.keys()):
        del state[key]
