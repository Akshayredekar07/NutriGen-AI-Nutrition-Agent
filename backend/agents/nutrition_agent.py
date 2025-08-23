from .base_agent import BaseAgent

class NutritionAgent(BaseAgent):
    def run(self, query: str) -> str:
        # Example: add domain-specific logic
        return f"NutritionAgent -> {super().run(query)}"
