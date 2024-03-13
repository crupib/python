from graphviz import Digraph

A = [[-3,  4,  0],
     [ 1, -4,  5],
     [ 2,  0, -5]]

N = len(A)

G = Digraph(format='png')
G.body.extend(['rankdir=LR'])

G.attr('node', shape='circle', fontsize="24", fontname="ipag")

for n in range(N):
    node = str(n)
    G.node(node)

for m in range(N):
    for n in range(N):
        s = A[m][n]
        if s != 0:
            s1 = f'{s}dt' if s > 0 else f'1{s}dt'
            node1 = str(n)
            node2 = str(m)
            label = str(s1)
            G.edge(node1, node2, label)

G.render('graph2')
