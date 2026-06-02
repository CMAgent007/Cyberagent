import requests
import json
import re

from memory_manager import remember, recall
from tool_registry import registry
from tools.knowledge import search_knowledge
from tools.file_agent import execute_file_action

registry.register(
    "shell",
    "tools.shell",
    "run_command"
)

SERVER_URL = "http://127.0.0.1:8080/completion"

SYSTEM_PROMPT = """
You are CyberAgent.

If a shell command is needed return ONLY JSON.

Examples:

{"action":"tool","tool":"shell","command":"pwd"}

{"action":"tool","tool":"shell","command":"ls"}

{"action":"tool","tool":"shell","command":"date"}

Otherwise answer normally.
"""

print("=" * 50)
print("CyberAgent V11")
print("Connected to llama-server")
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
            f"\nAgent:\nNice to meet you, {name}. I will remember that."
        )

        continue

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

    read_match = re.match(
        r"read\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if read_match:

        path = read_match.group(1).strip()

        result = execute_file_action(
            "read",
            path
        )

        print("\nAgent:\n")
        print(result)

        continue

    write_match = re.match(
        r"write\s+(\S+)\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if write_match:

        path = write_match.group(1)

        content = write_match.group(2)

        result = execute_file_action(
            "write",
            path,
            content
        )

        print("\nAgent:\n")
        print(result)

        continue

    append_match = re.match(
        r"append\s+(\S+)\s+(.+)",
        user_input,
        re.IGNORECASE
    )

    if append_match:

        path = append_match.group(1)

        content = append_match.group(2)

        result = execute_file_action(
            "append",
            path,
            content
        )

        print("\nAgent:\n")
        print(result)

        continue

    knowledge_result = search_knowledge(
        user_input
    )

    if knowledge_result:

        print("\nAgent:\n")
        print(knowledge_result)

        continue

    print("\nThinking...\n")

    try:

        response = requests.post(
            SERVER_URL,
            json={
                "prompt":
                    SYSTEM_PROMPT
                    + "\nUser: "
                    + user_input,
                "n_predict": 96,
                "temperature": 0.2,
                "stop": ["User:"]
            },
            timeout=120
        )

        data = response.json()

        reply = data["content"].strip()

    except Exception as e:

        print("\nError:")
        print(e)

        continue

    try:

        json_match = re.search(
            r"\{.*?\}",
            reply,
            re.DOTALL
        )

        if json_match:

            tool_call = json.loads(
                json_match.group(0)
            )

            if (
                tool_call.get("action")
                == "tool"
            ):

                success, result = registry.execute(
                    tool_call["tool"],
                    tool_call["command"]
                )

                print("\nAgent:\n")
                print(result)

                continue

    except Exception:
        pass

    print("\nAgent:\n")
    print(reply)
