class BaseTool:
    name: str = "base_tool"

    def run(self, query: str):
        raise NotImplementedError
