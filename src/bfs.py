from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search traversal.
    Returns list of nodes in BFS order.
    """

    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order