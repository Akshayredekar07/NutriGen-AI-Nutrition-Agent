from .base_tool import BaseTool

class SearchTool(BaseTool):
    name = "search"

    def run(self, query: str):
        return f"Searching for {query}"
