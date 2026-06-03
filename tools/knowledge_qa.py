import requests

from tools.knowledge import search_knowledge

SERVER_URL = "http://127.0.0.1:8080/completion"


def answer_from_knowledge(question):

    knowledge = search_knowledge(question)

    if not knowledge:

        return None

    prompt = f"""
You are CyberAgent.

Answer ONLY using the provided knowledge.

If the answer is not contained in the knowledge,
say:

I could not find that information in my knowledge base.

Knowledge:

{knowledge}

Question:
{question}

Answer:
"""

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt": prompt,
                "n_predict": 128,
                "temperature": 0.1,
                "stop": [
                    "Question:",
                    "Knowledge:"
                ]
            },
            timeout=120
        )

        data = response.json()

        return data["content"].strip()

    except Exception as e:

        return str(e)
