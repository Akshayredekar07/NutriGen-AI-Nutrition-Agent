from .search_tool import SearchTool
from .nutrition_api_tool import NutritionAPITool
from .calculator_tool import CalculatorTool

TOOLS = {
    "search": SearchTool(),
    "nutrition_api": NutritionAPITool(),
    "calculator": CalculatorTool(),
}
