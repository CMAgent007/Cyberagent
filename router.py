from tool_registry import registry

from tools.file_agent import execute_file_action
from tools.agent_builder import create_python_script
from tools.learning import learn_file


def execute_plan(plan):

    if plan is None:

        return None

    tool = plan.get("tool")

    # --------------------
    # SHELL
    # --------------------

    if tool == "shell":

        success, result = registry.execute(
            "shell",
            plan["command"]
        )

        return result

    # --------------------
    # FILES
    # --------------------

    if tool == "file":

        return execute_file_action(
            plan["action"],
            plan["path"],
            plan.get(
                "content",
                ""
            )
        )

    # --------------------
    # PYTHON
    # --------------------

    if tool == "python":

        success, result = registry.execute(
            "python",
            plan["path"]
        )

        return result

    # --------------------
    # SMART REPAIR
    # --------------------

    if tool == "smart_repair":

        success, result = registry.execute(
            "smart_repair"
        )

        return result

    # --------------------
    # SCRIPT BUILDER
    # --------------------

    if tool == "builder":

        return create_python_script(
            plan["prompt"]
        )

    # --------------------
    # LEARNING
    # --------------------

    if tool == "learning":

        return learn_file(
            plan["path"]
        )

    # --------------------
    # UNKNOWN
    # --------------------

    return "Unknown plan"
