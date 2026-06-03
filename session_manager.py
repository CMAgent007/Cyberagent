import json
import os

SESSION_FILE = "memory/session.json"


def load_session():

    if not os.path.exists(SESSION_FILE):

        return {}

    try:

        with open(
            SESSION_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {}


def save_session(data):

    os.makedirs(
        "memory",
        exist_ok=True
    )

    with open(
        SESSION_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def set_context(
    key,
    value
):

    data = load_session()

    data[key] = value

    save_session(data)


def get_context(key):

    data = load_session()

    return data.get(key)


def remove_context(key):

    data = load_session()

    if key in data:

        del data[key]

        save_session(data)


def clear_context():

    save_session({})


def get_all_context():

    return load_session()
