from typing import List, Dict, Any

class VectorStore:
    """Minimal in-memory vector store placeholder."""
    def __init__(self):
        self._store: List[Dict[str, Any]] = []

    def add(self, vector: List[float], metadata: Dict[str, Any]):
        self._store.append({"vector": vector, "metadata": metadata})

    def search(self, vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        # Return nearest neighbors (stub)
        return self._store[:top_k]
