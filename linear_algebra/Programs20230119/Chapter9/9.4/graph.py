from graphviz import Digraph

A = [[  0, 0.3, 0.3,   0, 0.5],
     [0.5, 0.2,   0,   0,   0],
     [  0, 0.5, 0.2,   0, 0.3],
     [  0,   0, 0.5, 0.5, 0.2],
     [0.5,   0,   0, 0.5,   0]]

N = len(A)

G = Digraph(format='jpg')
G.body.extend(['rankdir=LR'])

G.attr('node', shape='circle')

for n in range(N):
    node = str(n + 1)
    G.node(node)

for m in range(N):
    for n in range(N):
        s = A[m][n]
        if s != 0:
            node1 = str(n + 1)
            node2 = str(m + 1)
            label = str(s)
            G.edge(node1, node2, label)

G.render('graph')
