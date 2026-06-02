from tools.code_generator import generate_python_code
from tools.files import write_file


def build_script(
    prompt,
    output_file
):

    code = generate_python_code(
        prompt
    )

    write_file(
        output_file,
        code
    )

    return (
        f"Saved: {output_file}"
    )
