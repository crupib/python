from typing import Union
import networkx as nx
import matplotlib.pyplot as plt


class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight

    def print_edge(self):
        """Display the edge information in a human readable form."""
        print(f"{self.from_node} -> {self.to_node} = {self.weight}")
class Node:
    def __init__(self, index: int, label=None):
        self.index: int = index
        self.edges: dict = {}
        self.label: str = label
    def num_edges(self) -> int:
        return len(self.edges)
    def get_edge(self, neighbor: int) -> Union[Edge, None]:
        if neighbor in self.edges:
            return self.edges[neighbor]
        return None
    def add_edge(self, neighbor: int, weight: float):
        self.edges[neighbor] = Edge(self.index, neighbor,weight)
    def remove_edge(self, neighbor: int):
        if neighbor in self.edges:
            del self.edges[neighbor]
    def get_edge_list(self) -> list:
        return list(self.edges.values())
    def get_sorted_edge_list(self) -> list:
        result = []
        neighbors = (list)(self.edges.keys())
        neighbors.sort()
        for n in neighbors:
            result.append(self.edges[n])
        return result

class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]
    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edge(to_node)
    def is_edge(self, from_node: int, to_node: int) -> bool:
        return self.get_edge(from_node,to_node) is not None
    def make_edge_list(self) -> list:
        all_edges: list = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
        return all_edges
    def insert_edge(self, from_node: int, to_node: int, weight: float):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        self.nodes[from_node].add_edge(to_node, weight)
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)
    def remove_edge(self, from_node: int, to_node: int):
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        self.nodes[from_node].remove_edge(to_node)
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)
    def make_copy(self):
        """Create and return a copy of the graph."""
        g2: Graph = Graph(self.num_nodes, undirected=self.undirected)
        for node in self.nodes:
            g2.nodes[node.index].label = node.label
            for edge in node.edges.values():
                g2.insert_edge(edge.from_node, edge.to_node, edge.weight)
        return g2

def draw_graph(g: Graph):
    G = nx.DiGraph() if not g.undirected else nx.Graph()

    # add nodes
    for node in g.nodes:
        G.add_node(node.index)

    # add edges
    for edge in g.make_edge_list():
        G.add_edge(edge.from_node, edge.to_node, weight=edge.weight)

    # layout
    pos = nx.spring_layout(G)  # physics-based, good default

    # draw nodes (circles)
    nx.draw_networkx_nodes(
        G, pos,
        node_size=800,
        node_color="lightblue"
    )

    # draw edges (lines)
    nx.draw_networkx_edges(
        G, pos,
        arrowstyle="->",
        arrowsize=15
    )

    # draw labels
    nx.draw_networkx_labels(G, pos)

    # draw edge weights
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    g: Graph = Graph(5, undirected=False)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 3.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 4, 1.0)
    g.insert_edge(3, 4, 3.0)
    g.insert_edge(4, 2, 3.0)
    g.insert_edge(4, 3, 3.0)
    edge_list: list = g.make_edge_list()
    for edge in edge_list:
        edge.print_edge()
    draw_graph(g)