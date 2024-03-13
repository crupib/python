from numpy import *
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams["text.latex.preamble"] = r'''
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{stmaryrd}
\newcommand{\vv}[1]{\ensuremath{\boldsymbol{#1}}}
'''

p = array((0, 0))
q = array((2, 0))
t = linspace(0, 5, 1000)
x1 = 1 + sin(sqrt(2)*t)/sqrt(2)
x2 = (sqrt(2)*cos(sqrt(2)*t) + sin(sqrt(2)*t)) / (2*sqrt(2))
v1 = cos(sqrt(2*t))
v2 = (-sqrt(2)*sin(sqrt(2)*t) + cos(sqrt(2)*t)) / 2

plt.axis('scaled'), plt.xlim(-0.5,2.5), plt.ylim(-1,1.5)
plt.scatter(0, 0)
plt.scatter(2, 0)
plt.plot([0, x1[0]], [0, x2[0]])
plt.plot([2, x1[0]], [0, x2[0]])
plt.text(0, -0.02, r'$\vv{p}$', fontsize = 20,
         verticalalignment ='top', horizontalalignment ='center')
plt.text(2, -0.02, r'$\vv{q}$', fontsize = 20,
         verticalalignment ='top', horizontalalignment ='center')
plt.text(x1[0], x2[0], r'$\vv{x}\left(0\right)$', fontsize = 20,
         verticalalignment ='bottom', horizontalalignment ='right')

plt.plot(x1, x2)
plt.scatter(x1[0], x2[0])
plt.quiver(x1[0],  x2[0], v1[0], v2[0], units='xy', scale=1)
plt.text(x1[0]+v1[0]/2, x2[0]+v2[0]/2, r'$\vv{v}\left(0\right)$', fontsize = 20,
         verticalalignment ='bottom', horizontalalignment ='right')

#plt.show()
plt.savefig('exercise.png', bbox_inches='tight', pad_inches=0.05)
