from tools.code_generator import generate_python_code
from tools.files import write_file

from tools.validator import validate_python_code
from tools.code_fixer import fix_python_code


def build_script(
    prompt,
    output_file
):

    attempts = 3

    for attempt in range(attempts):

        print(
            f"Generation Attempt {attempt + 1}"
        )

        code = generate_python_code(
            prompt
        )

        valid, result = validate_python_code(
            code
        )

        if valid:

            write_file(
                output_file,
                code
            )

            return (
                f"Saved: {output_file}"
            )

        print(
            "Validation Failed"
        )

        print(
            result
        )

        code = fix_python_code(
            code,
            result
        )

        valid, result = validate_python_code(
            code
        )

        if valid:

            write_file(
                output_file,
                code
            )

            return (
                f"Saved after repair: {output_file}"
            )

    return (
        "Failed: Could not generate working code"
    )
