import subprocess


def run_python_file(path):

    try:

        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = ""

        if result.stdout:
            output += result.stdout

        if result.stderr:
            output += result.stderr

        return output

    except Exception as e:

        return str(e)
