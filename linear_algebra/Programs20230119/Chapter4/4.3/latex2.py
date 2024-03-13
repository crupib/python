from numpy.random import seed, choice
from sympy import Matrix, latex

seed(2021)
template = r'''
\begin{array}{ll}
(1) &%s%s =\\[0.5cm]
(2) &%s%s =\\[0.5cm]
(3) &%s%s =\\[0.5cm]
(4) &%s%s =\\[0.5cm]
(5) &%s%s =\\
\end{array}
'''

matrices= ()
for no in range(5):
    m, el, n = choice([2, 3], 3)
    X = [-3, -2, -1, 1, 2, 3, 4, 5]
    A = Matrix(choice(X, (m, el)))
    B = Matrix(choice(X, (el, n)))
    matrices += (latex(A), latex(B))
print(template % matrices)


'''
\begin{array}{ll}
(1) &\left[\begin{matrix}-3 & 3 & 4\\4 & 2 & 5\end{matrix}\right]\left[\begin{matrix}4 & 1 & 3\\3 & 3 & -3\\2 & 4 & 4\end{matrix}\right] =\\[0.5cm]
(2) &\left[\begin{matrix}3 & 5\\-2 & 4\end{matrix}\right]\left[\begin{matrix}-2 & 2 & 3\\-1 & -1 & -3\end{matrix}\right] =\\[0.5cm]
(3) &\left[\begin{matrix}-3 & -1 & 4\\1 & 2 & 3\\-3 & 3 & -2\end{matrix}\right]\left[\begin{matrix}4 & -1 & 4\\5 & 3 & 4\\-2 & 3 & 4\end{matrix}\right] =\\[0.5cm]
(4) &\left[\begin{matrix}2 & 3\\-1 & 1\\-2 & -1\end{matrix}\right]\left[\begin{matrix}-1 & 5\\-3 & -1\end{matrix}\right] =\\[0.5cm]
(5) &\left[\begin{matrix}1 & -2 & 4\\-2 & -2 & -1\end{matrix}\right]\left[\begin{matrix}5 & 3 & 1\\1 & 2 & 5\\5 & 1 & -2\end{matrix}\right] =\\
\end{array}
'''
