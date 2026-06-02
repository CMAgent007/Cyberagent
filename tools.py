import subprocess
import requests


def show_ip():

    try:

        ip = requests.get(
            "https://api.ipify.org",
            timeout=10
        ).text

        return f"Public IP: {ip}"

    except Exception as e:

        return str(e)


def show_disk():

    try:

        result = subprocess.check_output(
            "df -h",
            shell=True,
            text=True
        )

        return result

    except Exception as e:

        return str(e)


def show_memory():

    try:

        result = subprocess.check_output(
            "free -h",
            shell=True,
            text=True
        )

        return result

    except Exception as e:

        return str(e)
