import graphclass
from graphclass import Graph
from graphclass import Edge
from graphclass import Node
from graphclass import draw_graph
from GraphMatrix import GraphMatrix


def draw_graph_matrix(gm: GraphMatrix):
    print("Adjacency Matrix:")

    # print column headers
    header = "    " + "  ".join(f"{i}" for i in range(gm.num_nodes))
    print(header)

    # print each row with row label
    for i in range(gm.num_nodes):
        row = "  ".join(f"{gm.connections[i][j]:.1f}" for j in range(gm.num_nodes))
        print(f"{i} | {row}")

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
    gm = GraphMatrix(5, undirected=False)
    gm.set_edges(0, 1 , 1.0)
    gm.set_edges(0, 3, 1.0)
    gm.set_edges(0, 4, 3.0)
    gm.set_edges(1, 2, 2.0)
    gm.set_edges(1, 4, 1.0)
    gm.set_edges(3, 1, 1.0)
    gm.set_edges(4, 2, 3.0)
    gm.set_edges(4, 3, 3.0)
    draw_graph_matrix(gm)