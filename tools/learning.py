import os


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

            f.write(content)

        return (
            f"Learned: {output}"
        )

    except Exception as e:

        return str(e)
