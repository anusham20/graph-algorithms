class Graph:
    """
    Undirected graph implemented using an adjacency list.
    """

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  # Undirected graph

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])

    def get_vertices(self):
        return list(self.adj_list.keys())

    def __str__(self):
        return str(self.adj_list)