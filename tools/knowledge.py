import os

KNOWLEDGE_DIR = "knowledge"


def search_knowledge(query):

    query = query.lower()

    if not os.path.exists(KNOWLEDGE_DIR):
        return None

    results = []

    for filename in os.listdir(KNOWLEDGE_DIR):

        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(
            KNOWLEDGE_DIR,
            filename
        )

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            text = content.lower()

            words = query.split()

            for word in words:

                if len(word) < 3:
                    continue

                if word in text:

                    results.append(content)

                    break

        except Exception:
            pass

    if not results:
        return None

    return "\n\n".join(results)
