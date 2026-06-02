import re


def plan(user_input):

    text = user_input.lower().strip()

    # --------------------
    # SHELL COMMANDS
    # --------------------

    if (
        "current directory" in text
        or text == "pwd"
    ):

        return {
            "tool": "shell",
            "command": "pwd"
        }

    if (
        "list files" in text
        or text == "ls"
    ):

        return {
            "tool": "shell",
            "command": "ls"
        }

    if (
        "time" in text
        or "date" in text
    ):

        return {
            "tool": "shell",
            "command": "date"
        }

    # --------------------
    # FILE READ
    # --------------------

    match = re.match(
        r"read\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "file",
            "action": "read",
            "path": match.group(1).strip()
        }

    # --------------------
    # FILE WRITE
    # --------------------

    match = re.match(
        r"write\s+(\S+)\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "file",
            "action": "write",
            "path": match.group(1),
            "content": match.group(2)
        }

    # --------------------
    # FILE APPEND
    # --------------------

    match = re.match(
        r"append\s+(\S+)\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "file",
            "action": "append",
            "path": match.group(1),
            "content": match.group(2)
        }

    # --------------------
    # PYTHON EXECUTION
    # --------------------

    match = re.match(
        r"run\s+(.+\.py)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "python",
            "path": match.group(1).strip()
        }

    # --------------------
    # SCRIPT GENERATION
    # --------------------

    if (
        "create" in text
        and "script" in text
    ):

        return {
            "tool": "builder",
            "prompt": user_input
        }

    # --------------------
    # LEARNING TOOL
    # --------------------

    match = re.match(
        r"learn\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "learning",
            "path": match.group(1).strip()
        }

    # --------------------
    # NO TOOL FOUND
    # --------------------

    return None
