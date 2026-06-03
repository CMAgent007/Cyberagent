import os

KNOWLEDGE_DIR = "knowledge"


def search_knowledge(query):

    query = query.lower().strip()

    if not os.path.exists(KNOWLEDGE_DIR):

        return None

    results = []

    for filename in os.listdir(KNOWLEDGE_DIR):

        if not (
            filename.endswith(".txt")
            or filename.endswith(".md")
        ):
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

            matches = []

            for word in query.split():

                if len(word) < 3:
                    continue

                if word in text:

                    matches.append(word)

            if matches:

                results.append(
                    f"File: {filename}\n\n{content}"
                )

        except Exception:

            pass

    if not results:

        return None

    return "\n\n" + ("\n" + ("-" * 50) + "\n\n").join(results)
