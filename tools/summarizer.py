import requests

SERVER_URL = "http://127.0.0.1:8080/completion"


def summarize_text(text):

    prompt = f"""
You are a knowledge extraction system.

Read the text and return EXACTLY this format.

Summary:
(3-5 sentences maximum)

Key Concepts:
- concept
- concept
- concept
- concept
- concept

Text:

{text[:3000]}
"""

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt": prompt,
                "n_predict": 256,
                "temperature": 0.0
            },
            timeout=300
        )

        data = response.json()

        result = data["content"].strip()

        if "Summary:" not in result:

            result = (
                "Summary:\n"
                + result
            )

        return result

    except Exception as e:

        return (
            f"Summary failed: {e}"
        )
