from numpy import array, sqrt

def integral(f, dom):
    N = len(dom) - 1
    w = (dom[-1] - dom[0]) / N
    x = array([(dom[n] + dom[n + 1]) / 2 for n in range(N)])
    return sum(f(x)) * w

def inner(f, g, dom):
    return integral(lambda x: f(x).conj() * g(x), dom)

norm = {
    'L1': lambda f, dom: integral(lambda x: abs(f(x)), dom),
    'L2': lambda f, dom: sqrt(inner(f, f, dom)),
    'Loo': lambda f, dom: max(abs(f(dom))),
}

if __name__ == '__main__':
    from numpy import linspace, pi, sin, cos
    dom = linspace(0, pi, 1001)
    print(f'<sin|cos> = {inner(sin, cos, dom)}')
    print(f'||f_1||_2 = {norm["L2"](lambda x: x, dom)}')

'''
<sin|cos> = -3.6738427362813575e-18
||f_1||_2 = 3.214875266047432
'''
