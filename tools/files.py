import os


def read_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except Exception as e:

        return str(e)


def write_file(
    path,
    content
):

    try:

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)

        return (
            f"Saved: {path}"
        )

    except Exception as e:

        return str(e)


def append_file(
    path,
    content
):

    try:

        with open(
            path,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(content)

        return (
            f"Updated: {path}"
        )

    except Exception as e:

        return str(e)
