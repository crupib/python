import random
import time
from collections import deque, defaultdict
from heapq import heappush, heappop

# ---------------------------
# Algorithms
# ---------------------------

def dijkstra(graph, source):
    distances = {v: float('inf') for v in graph}
    distances[source] = 0.0
    pq = [(0.0, source)]
    visited = set()
    while pq:
        dist_u, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph[u].items():
            nd = dist_u + w
            if nd < distances[v]:
                distances[v] = nd
                heappush(pq, (nd, v))
    return distances

# --- "new_shortest_path" toy version + helpers (runnable) ---

def partition_into_layers(graph, source):
    """BFS layers by hop count from source."""
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
    return [layers_map[i] for i in range(len(layers_map))]

def find_influential_nodes(layer, distances, graph=None):
    """Nodes already discovered, ordered by best current distance."""
    return sorted((n for n in layer if n in distances), key=lambda n: distances[n])

def relax_from_node(node, distances, graph):
    for nb, w in graph.get(node, {}).items():
        cand = distances[node] + w
        if nb not in distances or cand < distances[nb]:
            distances[nb] = cand

def process_remaining_cluster(layer, distances, graph):
    """A few inner passes to propagate within the layer."""
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

def new_shortest_path(graph, source):
    layers = partition_into_layers(graph, source)
    distances = {source: 0.0}
    for layer in layers:
        influential = find_influential_nodes(layer, distances, graph)
        for node in influential:
            relax_from_node(node, distances, graph)
        process_remaining_cluster(layer, distances, graph)
    return distances

# ---------------------------
# Graph generators (undirected, weighted)
# ---------------------------

def add_edge(g, u, v, w):
    g.setdefault(u, {})
    g.setdefault(v, {})
    # If multiple edges generated, keep the lighter one
    if v not in g[u] or w < g[u][v]:
        g[u][v] = w
        g[v][u] = w

def make_toy_graph():
    # Same as earlier sample
    g = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
        'E': {'C': 10, 'D': 2, 'Z': 3},
        'Z': {'D': 6, 'E': 3}
    }
    return g, 'A'

def make_grid_graph(rows, cols, w_low=1, w_high=10):
    """
    2D grid (rows x cols) with 4-neighbor connectivity.
    Node labels: (r,c) tuples.
    """
    g = {}
    for r in range(rows):
        for c in range(cols):
            u = (r, c)
            g.setdefault(u, {})
            if r + 1 < rows:
                w = random.randint(w_low, w_high)
                add_edge(g, u, (r + 1, c), w)
            if c + 1 < cols:
                w = random.randint(w_low, w_high)
                add_edge(g, u, (r, c + 1), w)
    source = (0, 0)
    return g, source

def make_random_graph(n, avg_degree=4, w_low=1, w_high=10, seed=None):
    """
    Erdos–Renyi-ish undirected graph targeting ~ n*avg_degree/2 edges.
    Ensures connectedness by building a random spanning tree first.
    """
    if seed is not None:
        random.seed(seed)
    g = {}
    # Build a simple chain to ensure connectivity
    for i in range(n):
        g.setdefault(i, {})
        if i > 0:
            add_edge(g, i-1, i, random.randint(w_low, w_high))
    # Add extra random edges
    m_target = n * avg_degree // 2
    m_now = n - 1
    while m_now < m_target:
        u = random.randrange(n)
        v = random.randrange(n)
        if u == v:
            continue
        w = random.randint(w_low, w_high)
        if v not in g[u]:
            add_edge(g, u, v, w)
            m_now += 1
    source = 0
    return g, source

# ---------------------------
# Timing harness
# ---------------------------

def time_once(fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0)

def compare_and_time(graph, source):
    d_out, d_time = time_once(dijkstra, graph, source)
    n_out, n_time = time_once(new_shortest_path, graph, source)

    # Align keys (some nodes might be unreachable in weird graphs; here all are connected)
    all_nodes = set(graph.keys())
    ok = True
    for v in all_nodes:
        dv = d_out.get(v, float('inf'))
        nv = n_out.get(v, float('inf'))
        # Use a tiny tolerance because we're using floats
        if abs(dv - nv) > 1e-9:
            ok = False
            break
    return d_time, n_time, ok

def run_suite():
    random.seed(42)
    tests = []

    # 1) Toy
    g, s = make_toy_graph()
    tests.append(("toy-6", g, s))

    # 2) Grid graphs (structured, grows fairly predictably)
    for r, c in [(10, 10), (20, 20)]:  # 100 and 400 nodes
        g, s = make_grid_graph(r, c)
        tests.append((f"grid-{r}x{c}", g, s))

    # 3) Random graphs at different sizes/densities
    rand_specs = [
        (100, 4),
        (100, 10),
        (300, 6),
        (600, 6),
    ]
    for n, deg in rand_specs:
        g, s = make_random_graph(n, avg_degree=deg, seed=1234)
        tests.append((f"rand-n{n}-deg{deg}", g, s))

    # Run timings
    print("\n=== Shortest-Path Timing (seconds) ===")
    print(f"{'dataset':<18} {'|V|':>6} {'|E|':>8}  {'dijkstra':>10}  {'new_shortest':>14}  {'match?':>8}")
    print("-" * 70)
    for name, g, s in tests:
        n_nodes = len(g)
        n_edges = sum(len(neigh) for neigh in g.values()) // 2  # undirected
        d_time, n_time, ok = compare_and_time(g, s)
        print(f"{name:<18} {n_nodes:>6} {n_edges:>8}  {d_time:>10.6f}  {n_time:>14.6f}  {str(ok):>8}")

if __name__ == "__main__":
    run_suite()

