import os

from tools.summarizer import summarize_text


def learn_file(path):

    if not os.path.exists(path):

        return "File not found"

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        summary = summarize_text(
            content
        )

        filename = os.path.basename(path)

        output = os.path.join(
            "knowledge",
            filename
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(summary)

        return (
            f"Learned and summarized: {output}"
        )

    except Exception as e:

        return str(e)
