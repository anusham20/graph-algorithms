def dfs_recursive(graph, start, visited=None, order=None):
    """
    Depth-First Search (recursive).
    Returns traversal order.
    """

    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor, _ in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def dfs_iterative(graph, start):
    """
    Depth-First Search (iterative using stack).
    Returns traversal order.
    """

    visited = set()
    stack = [start]
    order = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)

            for neighbor, _ in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order