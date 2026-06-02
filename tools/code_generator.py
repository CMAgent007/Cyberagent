import requests
import re

SERVER_URL = "http://127.0.0.1:8080/completion"


def generate_python_code(prompt):

    system_prompt = """
You are a Python code generator.

Output ONLY executable Python code.

Rules:
- No explanations
- No markdown
- No ``` blocks
- No comments
- Do not add features not requested
- Generate the smallest working solution
- Return Python code only
"""

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt":
                    system_prompt
                    + "\nUser: "
                    + prompt,

                "n_predict": 256,

                "temperature": 0.0,

                "stop": [
                    "User:",
                    "Explanation:",
                    "Here is"
                ]
            },
            timeout=300
        )

        data = response.json()

        print(
            "DEBUG:",
            data.get(
                "stop_type",
                "unknown"
            )
        )

        text = data["content"].strip()

        # Extract code from markdown blocks

        code_blocks = re.findall(
            r"```(?:python)?(.*?)```",
            text,
            re.DOTALL
        )

        if code_blocks:

            return code_blocks[0].strip()

        # Remove obvious explanation lines

        cleaned = []

        skip_starts = [
            "here is",
            "the following",
            "this script",
            "example:",
            "save this",
            "output:"
        ]

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            should_skip = False

            for prefix in skip_starts:

                if lower.startswith(prefix):

                    should_skip = True

                    break

            if not should_skip:

                cleaned.append(line)

        result = "\n".join(cleaned)

        return result.strip()

    except Exception as e:

        return (
            f"# ERROR\n"
            f"# {str(e)}"
        )
