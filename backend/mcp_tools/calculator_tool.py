from .base_tool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"

    def run(self, query: str):
        return f"Calculated result for {query}"
