from numpy.random import choice, seed

s = 2021
W1 = W2 = [1, 2, 3, 4, 5, 6]

def X(w):
    return w[0] + w[1]

def X1(w1):
    return X((w1, choice(W2)))

seed(s)
for n in range(20):
    w1 = choice(W1)
    print(X1(w1), end=' ')
print()
seed(s)
for n in range(20):
    w = choice(W1), choice(W2)
    print(X(w), end=' ')

'''
11 3 11 10 12 6 8 4 11 6 5 3 7 11 7 5 8 8 6 11 
11 3 11 10 12 6 8 4 11 6 5 3 7 11 7 5 8 8 6 11 
'''
