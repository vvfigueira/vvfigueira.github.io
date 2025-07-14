from numpy import arange
from math import cos, pi
import matplotlib.pyplot as plt

def fG(t, vX, vV, vF):
    return 0.5 * vX * (1 -(4 * vX**2)) - 0.25 * vV + vF * cos(vFrequencia * t)

def RK4(t, vX, vV, vF, vPasso, vN):
    for i in range(vN):

        k1x = vPasso * vV
        k1v = vPasso * fG(t, vX, vV, vF)
        k2x = vPasso * (vV + 0.5 * k1v)
        k2v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k1x, vV + 0.5 * k1v, vF)
        k3x = vPasso * (vV + 0.5 * k2v)
        k3v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k2x, vV + 0.5 * k2v, vF)
        k4x = vPasso * (vV + k3v)
        k4v = vPasso * fG(t + vPasso, vX + k3x, vV + k3v, vF)

        vX += (k1x + 2 * (k2x + k3x) + k4x)/6
        vV += (k1v + 2 * (k2v + k3v) + k4v)/6

        t += vPasso
    return t, vX, vV

vFrequencia = 1

vX0 = -0.5
vV0 = 0.5

vTransiente = 200000
vPeriodo = 1000

tX = []
tF = []

for vF in arange(0, 0.35, 25e-5):
    t = 0
    vX = vX0
    vV = vV0

    vPasso = 0.01 * 2 * pi / vFrequencia

    t, vX, vV = RK4(t, vX, vV, vF, vPasso, vTransiente)

    vPasso = 0.001 * pi / vFrequencia

    for i in range(100):

        print("F = %f" %vF)

        t, vX, vV = RK4(t, vX, vV, vF, vPasso, vPeriodo)

        tX.append(vX)
        tF.append(vF)

plt.scatter(tF, tX, marker='.', s = 0.3)
plt.title("Diagrama de Bifurcação")
plt.xlabel("$F$")
plt.ylabel("$x$")
plt.show()
