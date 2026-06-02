import requests
import re

SERVER_URL = "http://127.0.0.1:8080/completion"


def fix_python_code(
    code,
    error
):

    system_prompt = """
You are a Python debugging assistant.

Your task is to fix Python code.

Rules:
- Return ONLY Python code
- No markdown
- No explanations
- No comments
- Fix the error
- Return the complete corrected script
"""

    prompt = f"""
Code:
{code}

Error:
{error}

Return the corrected Python code.
"""

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt":
                    system_prompt
                    + "\n"
                    + prompt,

                "n_predict": 512,

                "temperature": 0.0,

                "stop": [
                    "Explanation:",
                    "User:",
                    "Here is"
                ]
            },
            timeout=300
        )

        data = response.json()

        print(
            "FIX DEBUG:",
            data.get(
                "stop_type",
                "unknown"
            )
        )

        text = data["content"].strip()

        code_blocks = re.findall(
            r"```(?:python)?(.*?)```",
            text,
            re.DOTALL
        )

        if code_blocks:

            return code_blocks[0].strip()

        return text

    except Exception as e:

        return (
            f"# ERROR\n"
            f"# {str(e)}"
        )
