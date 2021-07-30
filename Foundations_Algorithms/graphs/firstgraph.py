import networkx as nx
G = nx.Graph()
G.add_node("Mike")
G.add_nodes_from(["Amine", "Wassim", "Nick"])
G.add_edge("Mike", "Amine")
G.add_edge("Amine", "Imran")
print(list(G.nodes))
print(list(G.edges))
