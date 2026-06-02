import re


def plan(user_input):

    text = user_input.lower().strip()

    # Shell commands

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

    # File read

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

    # File write

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

    # File append

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

    # Python execution

    match = re.match(
        r"run\s+(.+\.py)",
        user_input,
        re.IGNORECASE
    )

    if match:

        return {
            "tool": "python",
            "path": match.group(1)
        }

    # Script generation

    if (
        "create" in text
        and "script" in text
    ):

        return {
            "tool": "builder",
            "prompt": user_input
        }

    return None
