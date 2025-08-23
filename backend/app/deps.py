# Shared dependencies (DB, cache, agents, vectorstore, etc.)
from rag.pipeline import RAGPipeline
from agents.nutrition_agent import NutritionAgent

rag_pipeline = RAGPipeline()
nutrition_agent = NutritionAgent(rag_pipeline)
