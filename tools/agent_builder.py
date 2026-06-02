from tools.script_builder import build_script
import re


def create_python_script(prompt):

    text = prompt.lower()

    filename = "generated.py"

    keywords = [
        "calculator",
        "fibonacci",
        "todo",
        "server",
        "client",
        "scanner",
        "logger",
        "backup"
    ]

    for word in keywords:

        if word in text:

            filename = f"{word}.py"

            break

    path = f"workspace/{filename}"

    result = build_script(
        prompt,
        path
    )

    return result
