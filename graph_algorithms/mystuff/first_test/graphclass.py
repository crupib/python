from typing import Union
import networkx as nx
import matplotlib.pyplot as plt


class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight

    def print_edge(self):
        print(f"{self.from_node} -> {self.to_node} = {self.weight}")


class Node:
    def __init__(self, index: int, label=None):
        self.index: int = index
        self.edges: dict = {}
        self.label: str = label

    def num_edges(self) -> int:
        return len(self.edges)

    def get_edge(self, neighbor: int) -> Union[Edge, None]:
        return self.edges.get(neighbor)

    def add_edge(self, neighbor: int, weight: float):
        self.edges[neighbor] = Edge(self.index, neighbor, weight)

    def remove_edge(self, neighbor: int):
        self.edges.pop(neighbor, None)

    def get_edge_list(self) -> list:
        return list(self.edges.values())


class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(i) for i in range(num_nodes)]

    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]:
        return self.nodes[from_node].get_edge(to_node)

    def make_edge_list(self) -> list:
        edges = []
        for node in self.nodes:
            edges.extend(node.edges.values())
        return edges

    def insert_edge(self, from_node: int, to_node: int, weight: float):
        self.nodes[from_node].add_edge(to_node, weight)
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)


def draw_graph(g: Graph, title: str | None = None):
    G = nx.DiGraph() if not g.undirected else nx.Graph()

    for node in g.nodes:
        G.add_node(node.index)

    for edge in g.make_edge_list():
        G.add_edge(edge.from_node, edge.to_node, weight=edge.weight)

    # Increased spacing + stable layout
    pos = nx.spring_layout(G, k=1.2, seed=42)

    nx.draw_networkx_nodes(
        G, pos,
        node_size=800,
        node_color="lightblue"
    )

    nx.draw_networkx_edges(
        G, pos,
        arrowstyle="->",
        arrowsize=15,
        edge_color="red"   # 🔴 arrows are now red
    )

    nx.draw_networkx_labels(G, pos)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if title:
        plt.title(title, fontsize=14)

    plt.axis("off")
    plt.show()
