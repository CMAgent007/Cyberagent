from tool_registry import registry
from tools.file_agent import execute_file_action
from tools.agent_builder import create_python_script


def execute_plan(plan):

    if plan is None:

        return None

    tool = plan.get("tool")

    # Shell

    if tool == "shell":

        success, result = registry.execute(
            "shell",
            plan["command"]
        )

        return result

    # File

    if tool == "file":

        return execute_file_action(
            plan["action"],
            plan["path"],
            plan.get(
                "content",
                ""
            )
        )

    # Python

    if tool == "python":

        success, result = registry.execute(
            "python",
            plan["path"]
        )

        return result

    # Builder

    if tool == "builder":

        return create_python_script(
            plan["prompt"]
        )

    return "Unknown plan"
