import matplotlib.pyplot as plt

def fG(t, vX, vV, vGamma):
    return 0.5 * vX * (1 - 4 * vX**2) - 2 * vGamma * vV

def fRungeKutta4(t, vX, vV, vGamma, vPasso):

    k1x = vPasso * vV
    k1v = vPasso * fG(t, vX, vV, vGamma)
    k2x = vPasso * (vV + 0.5 * k1v)
    k2v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k1x, vV + 0.5 * k1v, vGamma)
    k3x = vPasso * (vV + 0.5 * k2v)
    k3v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k2x, vV + 0.5 * k2v, vGamma)
    k4x = vPasso * (vV + k3v)
    k4v = vPasso * fG(t + vPasso, vX + k3x, vV + k3v, vGamma)

    return (k1x + 2 * (k2x + k3x) + k4x)/6, (k1v + 2 * (k2v + k3v) + k4v)/6

vPasso = 0.01

vX0 = -0.5
vV0 = 0.5

tGamma = [0.25/2,0.8/2]

for vGamma in tGamma:

    tX = []
    tV = []

    vX = vX0
    vV = vV0

    tX.append(vX)
    tV.append(vV)
    
    t = 0

    while (t < 40):

        vDeltaX, vDeltaV = fRungeKutta4(t, vX, vV, vGamma, vPasso)

        vX += vDeltaX
        vV += vDeltaV

        tX.append(vX)
        tV.append(vV)

        t += vPasso

    plt.plot(tX, tV, label="2 gamma = %.2f" %(2*vGamma))

plt.title("Diagramas de espaço de fase")
plt.xlabel("$x(t)$")
plt.ylabel("$dot x(t)$")
plt.ylim(-1.1,1.1)
plt.xlim(-1.9,1.9)
plt.legend()
plt.show()
