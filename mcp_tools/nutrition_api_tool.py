from .base_tool import BaseTool

class NutritionAPITool(BaseTool):
    name = "nutrition_api"

    def run(self, query: str):
        return f"Fetching nutrition data for {query}"
