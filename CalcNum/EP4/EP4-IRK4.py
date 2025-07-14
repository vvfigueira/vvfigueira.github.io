def fG(t, fY, fDerivadaY):
    return fDerivadaY + fY - t**3 - 3 * t**2 + 7*t + 1

def fRungeKutta4(t, fY, fDerivadaY, vPasso):

    k1y = vPasso*fDerivadaY
    k1z = vPasso*fG(t, fY, fDerivadaY)
    k2y = vPasso*(fDerivadaY + 0.5 * k1z)
    k2z = vPasso*fG(t + 0.5 * vPasso, fY + 0.5 * k1y, fDerivadaY + 0.5 * k1z)
    k3y = vPasso*(fDerivadaY + 0.5 * k2z)
    k3z = vPasso*(fG(t + 0.5 * vPasso, fY + 0.5 * k2y, fDerivadaY + 0.5 * k2z))
    k4y = vPasso*(fDerivadaY + k3z)
    k4z = vPasso*fG(t + vPasso, fY + k3y, fDerivadaY + k3z)

    return (k1y + 2 * (k2y + k3y) + k4y)/6, (k1z + 2 * (k2z + k3z) + k4z)/6

vPasso = 0.01

fY0 = 0
fDerivadaY0 = -1

fY = fY0
fDerivadaY = fDerivadaY0

t = 0

while (t<=5):

    vDeltaY, vDeltaDerivadaY = fRungeKutta4(t, fY, fDerivadaY, vPasso)

    fY += vDeltaY
    fDerivadaY += vDeltaDerivadaY
    
    t += vPasso

print("y(5) = %.8f, z(5) = %.8f" %(fY, fDerivadaY))
print("y(5) = %.8f, z(5) = %.8f" %(5**3 - 5, 3 * 5**2 - 1))
