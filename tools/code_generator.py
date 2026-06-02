import requests
import re

SERVER_URL = "http://127.0.0.1:8080/completion"


def generate_python_code(prompt):

    system_prompt = """
Return ONLY Python code.

No explanations.

No markdown.

No comments.

Only executable Python.
"""

    response = requests.post(
        SERVER_URL,
        json={
            "prompt":
                system_prompt
                + "\nUser: "
                + prompt,
            "n_predict": 256,
            "temperature": 0.1,
            "stop": ["User:"]
        },
        timeout=120
    )

    data = response.json()

    text = data["content"].strip()

    code_blocks = re.findall(
        r"```(?:python)?(.*?)```",
        text,
        re.DOTALL
    )

    if code_blocks:

        return code_blocks[0].strip()

    lines = []

    for line in text.splitlines():

        line = line.rstrip()

        if (
            line.startswith("Here is")
            or line.startswith("Save this")
            or line.startswith("The following")
        ):
            continue

        lines.append(line)

    return "\n".join(lines).strip()
