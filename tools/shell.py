import subprocess

BLOCKED = [
    "rm",
    "reboot",
    "shutdown",
    "halt",
    "poweroff",
    "mkfs",
    "dd",
    ":(){:|:&};:"
]


def run_command(command):

    cmd = command.strip().lower()

    for item in BLOCKED:

        if item in cmd:

            return (
                "BLOCKED: Dangerous command detected."
            )

    try:

        result = subprocess.run(
            command,
            shell=True,
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
