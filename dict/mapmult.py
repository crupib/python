from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])
print(d['b'])
e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(e['a'])
print(e['b'])



