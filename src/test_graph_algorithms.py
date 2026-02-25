from graph import Graph
from bfs import bfs
from dfs import dfs_recursive, dfs_iterative


def build_sample_graph():
    g = Graph()
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E"),
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    return g


def test_bfs():
    g = build_sample_graph()
    result = bfs(g, "A")
    assert result == ["A", "B", "C", "D", "E"]
    print("✓ BFS test passed")


def test_dfs_recursive():
    g = build_sample_graph()
    result = dfs_recursive(g, "A")
    assert result == ["A", "B", "D", "E", "C"]
    print("✓ DFS Recursive test passed")


def test_dfs_iterative():
    g = build_sample_graph()
    result = dfs_iterative(g, "A")
    assert result == ["A", "B", "D", "E", "C"]
    print("✓ DFS Iterative test passed")


if __name__ == "__main__":
    test_bfs()
    test_dfs_recursive()
    test_dfs_iterative()