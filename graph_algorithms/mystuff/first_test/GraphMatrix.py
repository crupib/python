from graphclass import Graph


class GraphMatrix:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes = num_nodes
        self.undirected = undirected
        self.connections = [[0.0] * num_nodes for _ in range(num_nodes)]

    def get_edges(self, from_node: int, to_node: int) -> float:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        return self.connections[from_node][to_node]

    def set_edges(self, from_node: int, to_node: int, weight: float):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        self.connections[from_node][to_node] = weight
        if self.undirected:
            self.connections[to_node][from_node] = weight

    def to_graph(self) -> Graph:
        """Convert adjacency matrix to Graph (adjacency list)."""
        g = Graph(self.num_nodes, undirected=self.undirected)
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                weight = self.connections[i][j]
                if weight != 0.0:
                    g.insert_edge(i, j, weight)
        return g
