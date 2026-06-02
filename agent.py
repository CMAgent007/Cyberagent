import requests
import re

from memory_manager import remember, recall
from tools.knowledge import search_knowledge

from planner import plan
from router import execute_plan

SERVER_URL = "http://127.0.0.1:8080/completion"

SYSTEM_PROMPT = """
You are CyberAgent.

Be concise.

Answer clearly.

If you do not need a tool, answer normally.
"""

print("=" * 50)
print("CyberAgent V15")
print("Planner + Router Architecture")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() in [
        "exit",
        "quit"
    ]:
        break

    user_lower = user_input.lower()

    # --------------------
    # MEMORY STORE
    # --------------------

    match = re.search(
        r"my name is (.+)",
        user_input,
        re.IGNORECASE
    )

    if match:

        name = match.group(1).strip()

        remember(
            "name",
            name
        )

        print(
            f"\nAgent:\nNice to meet you, {name}."
        )

        continue

    # --------------------
    # MEMORY RECALL
    # --------------------

    if user_lower in [
        "what is my name",
        "whats my name"
    ]:

        name = recall("name")

        if name:

            print(
                f"\nAgent:\nYour name is {name}."
            )

        else:

            print(
                "\nAgent:\nI do not know your name yet."
            )

        continue

    # --------------------
    # KNOWLEDGE SEARCH
    # --------------------

    knowledge_result = search_knowledge(
        user_input
    )

    if knowledge_result:

        print("\nAgent:\n")
        print(knowledge_result)

        continue

    # --------------------
    # PLANNER
    # --------------------

    task = plan(
        user_input
    )

    if task:

        result = execute_plan(
            task
        )

        print("\nAgent:\n")
        print(result)

        continue

    # --------------------
    # LLM FALLBACK
    # --------------------

    print("\nThinking...\n")

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt":
                    SYSTEM_PROMPT
                    + "\nUser: "
                    + user_input,
                "n_predict": 128,
                "temperature": 0.3,
                "stop": ["User:"]
            },
            timeout=120
        )

        data = response.json()

        reply = data["content"].strip()

        print("\nAgent:\n")
        print(reply)

    except Exception as e:

        print("\nError:")
        print(e)
