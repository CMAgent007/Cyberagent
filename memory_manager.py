import json
import os

FACTS_FILE = "memory/facts.json"


def ensure_memory_file():

    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(FACTS_FILE):

        with open(
            FACTS_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump({}, f)


def load_facts():

    ensure_memory_file()

    try:

        with open(
            FACTS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {}


def save_facts(facts):

    ensure_memory_file()

    with open(
        FACTS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            facts,
            f,
            indent=4
        )


def remember(key, value):

    facts = load_facts()

    facts[key] = value

    save_facts(facts)


def recall(key):

    facts = load_facts()

    return facts.get(key)


def forget(key):

    facts = load_facts()

    if key in facts:

        del facts[key]

        save_facts(facts)


def get_all_facts():

    return load_facts()
