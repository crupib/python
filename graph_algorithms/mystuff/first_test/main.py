import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

from graphclass import Graph, draw_graph_on_axes
from GraphMatrix import GraphMatrix


def edge_keys(g: Graph):
    """Return set of (u, v) edge keys from a Graph."""
    return {(e.from_node, e.to_node) for e in g.make_edge_list()}


# =========================================================
# Build LINEAR (Adjacency List) Graph
# =========================================================
g_linear = Graph(5, undirected=False)
edges = [
    (0, 1, 1.0),
    (0, 3, 1.0),
    (0, 4, 3.0),
    (1, 2, 2.0),
    (1, 4, 1.0),
    (3, 4, 3.0),
    (4, 2, 3.0),
    (4, 3, 3.0)
]

for u, v, w in edges:
    g_linear.insert_edge(u, v, w)


# =========================================================
# Build MATRIX Graph (Adjacency Matrix)
# =========================================================
gm = GraphMatrix(5, undirected=False)

# (You can remove or add edges here to test differences)
for u, v, w in edges:
    gm.set_edges(u, v, w)

g_matrix = gm.to_graph()


# =========================================================
# Shared Layout (EXACT same node positions)
# =========================================================
nx_base = nx.DiGraph()
nx_base.add_nodes_from(range(5))

pos = nx.spring_layout(
    nx_base,
    seed=42,   # deterministic layout
    k=1.2      # spacing
)


# =========================================================
# Compute Differences
# =========================================================
linear_edges = edge_keys(g_linear)
matrix_edges = edge_keys(g_matrix)

only_in_linear = linear_edges - matrix_edges
only_in_matrix = matrix_edges - linear_edges


# =========================================================
# Matplotlib Figure (Side-by-Side)
# =========================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), constrained_layout=True)


def update(frame):
    """Animation step: progressively reveal differences."""
    ax1.clear()
    ax2.clear()

    draw_graph_on_axes(
        ax=ax1,
        g=g_linear,
        pos=pos,
        title="Linear Graph (Adjacency List)",
        highlight_edges=list(only_in_linear)[:frame + 1]
    )

    draw_graph_on_axes(
        ax=ax2,
        g=g_matrix,
        pos=pos,
        title="Matrix Graph (Adjacency Matrix)",
        highlight_edges=list(only_in_matrix)[:frame + 1]
    )


frames = max(len(only_in_linear), len(only_in_matrix)) + 1

ani = animation.FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=1000,
    repeat=False
)


# =========================================================
# Color Legend (Horizontal at bottom)
# =========================================================
all_weights = [e.weight for e in g_linear.make_edge_list()]

sm = ScalarMappable(
    norm=Normalize(min(all_weights), max(all_weights)),
    cmap="viridis"
)
sm.set_array([])

# Add colorbar below both subplots
cbar_ax = fig.add_axes([0.15, 0.05, 0.7, 0.03])  # left, bottom, width, height
fig.colorbar(sm, cax=cbar_ax, orientation='horizontal', label="Edge Weight")


# =========================================================
# Show Figure
# =========================================================
plt.show()
