from typing import Iterable
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import mplcursors


class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


class Node:
    def __init__(self, index: int):
        self.index = index
        self.edges = {}

    def add_edge(self, neighbor: int, weight: float):
        self.edges[neighbor] = Edge(self.index, neighbor, weight)
    def get_neighbors(self) -> set:
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors
    def get_out_neighbors(self) -> set:
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors


class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes = num_nodes
        self.undirected = undirected
        self.nodes = [Node(i) for i in range(num_nodes)]

    def insert_edge(self, u: int, v: int, w: float):
        self.nodes[u].add_edge(v, w)
        if self.undirected:
            self.nodes[v].add_edge(u, w)

    def make_edge_list(self):
        edges = []
        for node in self.nodes:
            edges.extend(node.edges.values())
        return edges
    # inefficient
    def get_in_neighbors(self, target:int) -> set:
        neighbors: set = set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)
        return neighbors
    def make_undirected_neighborhood_subgraph(self, ind: int, closed: bool):
        """Create the subgraph of neighbors to a given node in an undirected graph.

        Parameters
        ----------
        ind : int
            The index of the query node.
        closed : bool
            Indicates whether to include the given node (True) or not (False).

        Returns
        -------
        g_new : Graph
            The subgraph consisting of the node's neighborhood.
        """
        if not self.undirected:
            raise ValueError

        nodes_to_use: set = self.nodes[ind].get_neighbors()
        if closed:
            nodes_to_use.add(ind)

        index_map = {}
        for new_index, old_index in enumerate(nodes_to_use):
            index_map[old_index] = new_index

        g_new: Graph = Graph(len(nodes_to_use), undirected=True)
        for n in nodes_to_use:
            for edge in self.nodes[n].get_edge_list():
                if edge.to_node in nodes_to_use and edge.to_node > n:
                    ind1_new = index_map[n]
                    ind2_new = index_map[edge.to_node]
                    g_new.insert_edge(ind1_new, ind2_new, edge.weight)

        return g_new

def draw_graph_on_axes(
    ax,
    g: Graph,
    pos,
    title: str,
    highlight_edges: Iterable[tuple[int, int]] = (),
    show_hover: bool = True
):
    G = nx.DiGraph() if not g.undirected else nx.Graph()

    edge_list = []
    weights = []

    for e in g.make_edge_list():
        G.add_edge(e.from_node, e.to_node, weight=e.weight)
        edge_list.append((e.from_node, e.to_node))
        weights.append(e.weight)

    # ---- Correct normalization ----
    norm = colors.Normalize(vmin=min(weights), vmax=max(weights))
    cmap = cm.viridis

    edge_colors = [cmap(norm(G[u][v]["weight"])) for u, v in edge_list]
    edge_widths = [
        4.0 if (u, v) in highlight_edges else 2.5
        for u, v in edge_list
    ]

    nx.draw_networkx_nodes(
        G, pos,
        node_size=900,
        node_color="lightblue",
        ax=ax
    )

    edges = nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edge_list,        # 🔑 explicit ordering
        edge_color=edge_colors,
        width=edge_widths,
        arrows=True,
        arrowstyle="->",
        arrowsize=30,              # bigger arrows
        connectionstyle="arc3,rad=0.25",
        ax=ax
    )

    nx.draw_networkx_labels(G, pos, ax=ax)

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(u, v): G[u][v]["weight"] for u, v in edge_list},
        ax=ax
    )

    ax.set_title(title)
    ax.axis("off")

    # ---- Hover labels ----
    if show_hover:
        cursor = mplcursors.cursor(edges, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            u, v = edge_list[sel.index]
            w = G[u][v]["weight"]
            sel.annotation.set_text(f"{u} → {v}\nweight = {w}")
