from graph import Graph
from bfs import bfs
from dfs import dfs_recursive, dfs_iterative
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from johnson import johnson

def main():
    g = Graph(directed=True)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "F", 11)

    print("Graph:", g)
    print("BFS from A:", bfs(g, "A"))
    print("DFS recursive from A:", dfs_recursive(g, "A"))
    print("DFS iterative from A:", dfs_iterative(g, "A"))
    print("Dijkstra from A:", dijkstra(g, "A"))
    print("Bellman-Ford from A:", bellman_ford(g, "A"))
    print("Johnson all-pairs shortest paths:", johnson(g))

if __name__ == "__main__":
    main()