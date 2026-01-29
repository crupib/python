from graphclass import Graph, draw_graph
from GraphMatrix import GraphMatrix


def print_graph_matrix(gm: GraphMatrix):
    print("Adjacency Matrix:")
    header = "    " + "  ".join(str(i) for i in range(gm.num_nodes))
    print(header)

    for i in range(gm.num_nodes):
        row = "  ".join(f"{gm.connections[i][j]:.1f}" for j in range(gm.num_nodes))
        print(f"{i} | {row}")


if __name__ == "__main__":
    # ===== Linear Graph =====
    g = Graph(5, undirected=False)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 3.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 4, 1.0)
    g.insert_edge(3, 4, 3.0)
    g.insert_edge(4, 2, 3.0)
    g.insert_edge(4, 3, 3.0)

    draw_graph(g, title="Linear Graph (Adjacency List)")

    # ===== Matrix Graph =====
    gm = GraphMatrix(5, undirected=False)
    gm.set_edges(0, 1, 1.0)
    gm.set_edges(0, 3, 1.0)
    gm.set_edges(0, 4, 3.0)
    gm.set_edges(1, 2, 2.0)
    gm.set_edges(1, 4, 1.0)
    gm.set_edges(3, 4, 3.0)
    gm.set_edges(4, 2, 3.0)
    gm.set_edges(4, 3, 3.0)

    print_graph_matrix(gm)

    g_from_matrix = gm.to_graph()
    draw_graph(g_from_matrix, title="Matrix Graph (Adjacency Matrix)")
