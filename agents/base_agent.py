class BaseAgent:
    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline

    def run(self, query: str) -> str:
        return self.rag_pipeline.run(query)
