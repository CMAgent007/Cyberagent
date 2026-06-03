from tools.script_builder import build_script
from session_manager import set_context


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

    if result.startswith("Saved"):

        set_context(
            "last_file",
            path
        )

    return result
