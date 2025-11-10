from collections import deque, defaultdict

# --- Helpers: simple, runnable interpretations ---

def partition_into_layers(graph, source):
    """BFS layers by hop-count from source."""
    layers_map = defaultdict(list)
    seen = {source}
    q = deque([(source, 0)])
    while q:
        node, d = q.popleft()
        layers_map[d].append(node)
        for nb in graph.get(node, {}):
            if nb not in seen:
                seen.add(nb)
                q.append((nb, d + 1))
    # turn into ordered list of layers [L0, L1, ...]
    return [layers_map[i] for i in range(len(layers_map))]

def find_influential_nodes(layer, distances, graph=None):
    """Nodes in this layer already discovered, ordered by current best distance."""
    return sorted((n for n in layer if n in distances), key=lambda n: distances[n])

def relax_from_node(node, distances, graph):
    """Standard relaxation from a single node to all its neighbors."""
    for nb, w in graph.get(node, {}).items():
        cand = distances[node] + w
        if nb not in distances or cand < distances[nb]:
            distances[nb] = cand

def process_remaining_cluster(layer, distances, graph):
    """
    One simple pass (with a few repeats) to propagate distances
    within the current layer using any newly improved nodes.
    """
    for _ in range(len(layer)):
        changed = False
        for u in layer:
            if u in distances:
                for v, w in graph.get(u, {}).items():
                    if v in layer:
                        cand = distances[u] + w
                        if v not in distances or cand < distances[v]:
                            distances[v] = cand
                            changed = True
        if not changed:
            break

# --- The algorithm under test ---

def new_shortest_path(graph, source):
    layers = partition_into_layers(graph, source)
    distances = {source: 0}
    for layer in layers:
        influential = find_influential_nodes(layer, distances, graph)
        for node in influential:
            relax_from_node(node, distances, graph)
        process_remaining_cluster(layer, distances, graph)
    return distances

# --- Example graph (adjacency list) ---

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

# Run it
print("Layers:", partition_into_layers(graph, 'A'))
print("Distances:", new_shortest_path(graph, 'A'))

