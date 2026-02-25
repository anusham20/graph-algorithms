from graph import Graph
from bfs import bfs
from dfs import dfs_recursive, dfs_iterative


def main():
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

    print("Graph:", g)
    print("BFS:", bfs(g, "A"))
    print("DFS Recursive:", dfs_recursive(g, "A"))
    print("DFS Iterative:", dfs_iterative(g, "A"))


if __name__ == "__main__":
    main()