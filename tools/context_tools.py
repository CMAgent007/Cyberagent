from session_manager import (
    get_context,
    remove_context
)


def current_file():

    file_path = get_context(
        "last_file"
    )

    if not file_path:

        return (
            "No current file"
        )

    return (
        f"Current file: {file_path}"
    )


def clear_current_file():

    remove_context(
        "last_file"
    )

    return (
        "Current file cleared"
    )
