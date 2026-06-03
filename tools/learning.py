import os
import shutil


def learn_file(path):

    if not os.path.exists(path):

        return "File not found"

    try:

        filename = os.path.basename(path)

        output = os.path.join(
            "knowledge",
            filename
        )

        os.makedirs(
            "knowledge",
            exist_ok=True
        )

        shutil.copy2(
            path,
            output
        )

        return (
            f"Learned: {output}"
        )

    except Exception as e:

        return str(e)
