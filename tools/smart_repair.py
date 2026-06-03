from session_manager import get_context

from tools.files import read_file
from tools.files import write_file

from tools.validator import validate_python_code
from tools.code_fixer import fix_python_code


def repair_last_file():

    last_file = get_context(
        "last_file"
    )

    if not last_file:

        return (
            "No active file found"
        )

    code = read_file(
        last_file
    )

    valid, result = validate_python_code(
        code
    )

    if valid:

        return (
            f"No errors found in {last_file}"
        )

    repaired_code = fix_python_code(
        code,
        result
    )

    valid, repair_result = validate_python_code(
        repaired_code
    )

    if not valid:

        return (
            "Repair failed:\n\n"
            + repair_result
        )

    write_file(
        last_file,
        repaired_code
    )

    return (
        f"Repaired: {last_file}"
    )
