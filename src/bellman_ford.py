def bellman_ford(graph, start):
    distances = {v: float("inf") for v in graph.get_vertices()}
    distances[start] = 0
    edges = graph.get_edges()

    for _ in range(len(graph.get_vertices()) - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances