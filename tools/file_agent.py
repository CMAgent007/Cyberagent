from tools.files import read_file
from tools.files import write_file
from tools.files import append_file


def execute_file_action(
    action,
    path,
    content=""
):

    if action == "read":

        return read_file(path)

    if action == "write":

        return write_file(
            path,
            content
        )

    if action == "append":

        return append_file(
            path,
            content
        )

    return "Unknown action"
