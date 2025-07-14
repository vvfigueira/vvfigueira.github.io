import matplotlib.pyplot as plt

def fG(t, vX):
    return 0.5 * vX * (1 - 4 * vX**2)

def fRungeKutta4(t, vX, vV, vPasso):

    k1x = vPasso * vV
    k1v = vPasso * fG(t, vX)
    k2x = vPasso * (vV + 0.5 * k1v)
    k2v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k1x)
    k3x = vPasso * (vV + 0.5 * k2v)
    k3v = vPasso * fG(t + 0.5 * vPasso, vX + 0.5 * k2x)
    k4x = vPasso * (vV + k3v)
    k4v = vPasso * fG(t + vPasso, vX + k3x)

    return (k1x + 2 * (k2x + k3x) + k4x)/6, (k1v + 2 * (k2v + k3v) + k4v)/6

vPasso = 0.01

vX0 = -0.5

for i in range(3):

    tX = []
    tV = []

    if i == 0:

        vV0 = 0.1

    elif i == 1:

        vV0 = 0.25

    else:

        vV0 = 0.5

    vX = vX0
    vV = vV0

    tX.append(vX)
    tV.append(vV)
    
    t = 0

    while (t<40):

        vDeltaX, vDeltaV = fRungeKutta4(t, vX, vV, vPasso)

        vX += vDeltaX
        vV += vDeltaV
        t += vPasso

        tX.append(vX)
        tV.append(vV)

    plt.plot(tX, tV, label="dot x(0) = %.2f" %(vV0))

plt.title("Diagramas de espaço de fase")
plt.xlabel("$x(t)$")
plt.ylabel("$dot x(t)$")
plt.legend()
plt.show()
