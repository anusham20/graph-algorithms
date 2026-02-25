class Graph:
    """
    Graph supporting:
    - Directed or undirected
    - Weighted edges
    """

    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        self.adj_list[v1].append((v2, weight))

        if not self.directed:
            self.adj_list[v2].append((v1, weight))

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                if self.directed or (v, u, w) not in edges:
                    edges.append((u, v, w))
        return edges

    def __str__(self):
        return str(self.adj_list)