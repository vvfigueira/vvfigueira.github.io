import numpy as np
import matplotlib.pyplot as plt

def fG(t, vX, vV, vF):
    return 0.5 * vX * (1 - 4 * vX**2) - 0.25 * vV + vF * np.cos(vOmega * t)

def fRungeKutta4(t, vX, vV, vF, vPasso, vN):

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

vPasso = 0.01

vX0 = -0.5
vV0 = 0.5
vOmega = 1

tF = [0.35]#0.11,0.115,0.14]

for vF in tF:

    tX = []
    tV = []

    t = 0

    t, vX, vV = fRungeKutta4(t, vX0, vV0, vF, vPasso, 200000)

    for i in range(15000):

        t, vX, vV = fRungeKutta4(t, vX, vV, vF, vPasso, 1)

        tX.append(vX)
        tV.append(vV)

    plt.plot(tX, tV, label="F = %.3f" %(vF))
    
    plt.title("Diagramas de espaço de fase")
    plt.xlabel("$x(t)$")
    plt.ylabel("$dot x(t)$")
    plt.ylim(-1.1,1.1)
    plt.xlim(-1.9,1.9)
    plt.grid()
    plt.legend()
    plt.show()
