# Graph Algorithms 📊

This repository contains implementations of fundamental **graph algorithms** in Python. It supports **directed** and **undirected graphs**, **weighted edges**, and includes demo and test scripts.

---

## 📂 Project Structure

graph-algorithms/
├── src/
│   ├── graph.py            # Graph class (directed/undirected, weighted)
│   ├── bfs.py              # Breadth-First Search
│   ├── dfs.py              # Depth-First Search (recursive & iterative)
│   ├── dijkstra.py         # Dijkstra’s shortest path
│   ├── bellman_ford.py     # Bellman-Ford shortest path
│   ├── johnson.py          # Johnson’s all-pairs shortest paths
│   ├── demo.py             # Demo of all algorithms
│   └── test_graph_algorithms.py # Unit tests using pytest
└── README.md

---

## 🧰 Features

- **Graph Class**  
  - Supports `directed` or `undirected` graphs
  - Weighted edges
  - Methods: `add_vertex`, `add_edge`, `get_neighbors`, `get_vertices`, `get_edges`
  
- **Algorithms Implemented**
  | Algorithm | Description |
  |-----------|-------------|
  | BFS 🌐 | Breadth-first search traversal |
  | DFS 🌲 | Depth-first search traversal (recursive & iterative) |
  | Dijkstra 🚀 | Shortest path for weighted graphs with non-negative weights |
  | Bellman-Ford ⚡ | Shortest path handling negative weights; detects negative cycles |
  | Johnson 🧩 | All-pairs shortest paths for sparse graphs |

---

## 🔹 Usage Example

```python
from src.graph import Graph
from src.bfs import bfs
from src.dfs import dfs_recursive, dfs_iterative
from src.dijkstra import dijkstra
from src.bellman_ford import bellman_ford
from src.johnson import johnson

g = Graph(directed=True)
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "C", 5)
g.add_edge("B", "D", 10)
g.add_edge("C", "E", 3)
g.add_edge("E", "D", 4)
g.add_edge("D", "F", 11)

print("BFS from A:", bfs(g, "A"))
print("DFS recursive from A:", dfs_recursive(g, "A"))
print("DFS iterative from A:", dfs_iterative(g, "A"))
print("Dijkstra from A:", dijkstra(g, "A"))
print("Bellman-Ford from A:", bellman_ford(g, "A"))
print("Johnson all-pairs shortest paths:", johnson(g))


⸻

✅ Running Tests

pip install pytest
pytest src/test_graph_algorithms.py

All algorithms are tested for correctness.

⸻

🎯 Learning Outcomes
	•	Understanding graph representations (adjacency list)
	•	Difference between directed and undirected graphs
	•	Traversals: BFS vs DFS
	•	Single-source shortest path: Dijkstra vs Bellman-Ford
	•	All-pairs shortest path: Johnson’s algorithm
	•	Writing unit tests for algorithms

⸻

🌟 Notes
	•	Weighted edges are supported in all algorithms
	•	Bellman-Ford handles negative weights, Dijkstra assumes non-negative weights
	•	Johnson’s algorithm combines Bellman-Ford + Dijkstra for all-pairs shortest paths

⸻

# 👩‍💻 Author

Anusha Maheshwari  