from graph import Graph
from bfs import bfs
from dfs import dfs_recursive, dfs_iterative
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from johnson import johnson

def create_test_graph():
    g = Graph(directed=True)
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("A", "C", 4)
    return g

def test_bfs():
    g = create_test_graph()
    assert bfs(g, "A") == ["A", "B", "C"]

def test_dfs():
    g = create_test_graph()
    assert dfs_recursive(g, "A") == ["A", "B", "C"]
    assert dfs_iterative(g, "A") == ["A", "B", "C"]

def test_dijkstra():
    g = create_test_graph()
    distances = dijkstra(g, "A")
    assert distances["C"] == 3

def test_bellman_ford():
    g = create_test_graph()
    distances = bellman_ford(g, "A")
    assert distances["C"] == 3

def test_johnson():
    g = create_test_graph()
    all_pairs = johnson(g)
    assert all_pairs["A"]["C"] == 3