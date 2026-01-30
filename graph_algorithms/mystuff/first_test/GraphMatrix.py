from graphclass import Graph


class GraphMatrix:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes = num_nodes
        self.undirected = undirected
        self.connections = [[0.0] * num_nodes for _ in range(num_nodes)]

    def set_edges(self, u: int, v: int, w: float):
        self.connections[u][v] = w
        if self.undirected:
            self.connections[v][u] = w

    def to_graph(self) -> Graph:
        g = Graph(self.num_nodes, undirected=self.undirected)
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.connections[i][j] != 0:
                    g.insert_edge(i, j, self.connections[i][j])
        return g
