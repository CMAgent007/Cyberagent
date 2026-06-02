import importlib


class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(
        self,
        name,
        module_path,
        function_name
    ):

        self.tools[name] = {
            "module": module_path,
            "function": function_name
        }

    def execute(
        self,
        tool_name,
        *args,
        **kwargs
    ):

        if tool_name not in self.tools:

            return (
                False,
                f"Unknown tool: {tool_name}"
            )

        try:

            tool_info = self.tools[tool_name]

            module = importlib.import_module(
                tool_info["module"]
            )

            function = getattr(
                module,
                tool_info["function"]
            )

            result = function(
                *args,
                **kwargs
            )

            return (
                True,
                result
            )

        except Exception as e:

            return (
                False,
                str(e)
            )


registry = ToolRegistry()
