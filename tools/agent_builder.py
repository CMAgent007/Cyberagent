from tools.script_builder import build_script


def create_python_script(prompt):

    filename = "workspace/generated.py"

    result = build_script(
        prompt,
        filename
    )

    return result
