import ast
import subprocess
import tempfile
import os


def validate_python_code(code):

    try:

        ast.parse(code)

    except Exception as e:

        return False, f"Syntax Error: {e}"

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as f:

            f.write(code)

            temp_path = f.name

        result = subprocess.run(
            ["python", temp_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        os.unlink(temp_path)

        if result.returncode != 0:

            return (
                False,
                result.stderr
            )

        return (
            True,
            result.stdout
        )

    except Exception as e:

        return (
            False,
            str(e)
        )
