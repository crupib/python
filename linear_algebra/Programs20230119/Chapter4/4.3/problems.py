from numpy import array

A = array([[1, 2], [3, 4]])
B = array([[1, 2, 3], [4, 5, 6]])
C = array([[1, 2], [3, 4], [5, 6]])
D = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for X in (A, B, C, D):
    for Y in (A, B, C, D):
        if X.shape[1] == Y.shape[0]:
            print(f'{X}\n{Y}\n= {X.dot(Y)}\n')

'''
[[1 2]
 [3 4]]
[[1 2]
 [3 4]]
= [[ 7 10]
 [15 22]]

[[1 2]
 [3 4]]
[[1 2 3]
 [4 5 6]]
= [[ 9 12 15]
 [19 26 33]]

[[1 2 3]
 [4 5 6]]
[[1 2]
 [3 4]
 [5 6]]
= [[22 28]
 [49 64]]

[[1 2 3]
 [4 5 6]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
= [[30 36 42]
 [66 81 96]]

[[1 2]
 [3 4]
 [5 6]]
[[1 2]
 [3 4]]
= [[ 7 10]
 [15 22]
 [23 34]]

[[1 2]
 [3 4]
 [5 6]]
[[1 2 3]
 [4 5 6]]
= [[ 9 12 15]
 [19 26 33]
 [29 40 51]]

[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2]
 [3 4]
 [5 6]]
= [[ 22  28]
 [ 49  64]
 [ 76 100]]

[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
= [[ 30  36  42]
 [ 66  81  96]
 [102 126 150]]
'''