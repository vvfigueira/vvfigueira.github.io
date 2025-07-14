from math import cos, pi
from numpy import arange
import matplotlib.pyplot as plt

def f(x):
    ''' Funcao que toma um valor de x e calcula o valor da funcao
        f(x) = x^3 - cos(x) neste ponto '''

    f = x**3 - cos(x)

    return f

def g(x):

    g = x**3

    return g

def h(x):

    h = -cos(x)

    return h

X = []
F = []
G = []
H = []

for x in arange(-pi/2,pi/2,0.001):

    X.append(x)

    F.append(f(x))
    G.append(g(x))
    H.append(h(x))

plt.plot(X,F,label="$f(x) = x^3 - cos(x)$")
plt.plot(X,G,label="$g(x) = x^3$")
plt.plot(X,H,label="$-h(x) = - cos(x)$")
plt.title("Análise de raízes")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
