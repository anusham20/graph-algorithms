from graph import Graph
from bellman_ford import bellman_ford
from dijkstra import dijkstra

def johnson(graph):
    new_graph = Graph(directed=True)
    for v in graph.get_vertices():
        new_graph.add_vertex(v)

    s = "__super_source__"
    new_graph.add_vertex(s)
    for v in graph.get_vertices():
        new_graph.add_edge(s, v, 0)

    for u, v, w in graph.get_edges():
        new_graph.add_edge(u, v, w)

    h = bellman_ford(new_graph, s)

    reweighted = Graph(directed=True)
    for u, v, w in graph.get_edges():
        reweighted.add_edge(u, v, w + h[u] - h[v])

    all_pairs = {}
    for v in graph.get_vertices():
        distances = dijkstra(reweighted, v)
        all_pairs[v] = {u: distances[u] - h[v] + h[u] for u in distances}

    return all_pairs