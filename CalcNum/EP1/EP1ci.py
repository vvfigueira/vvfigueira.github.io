import math
import numpy as np
import matplotlib.pyplot as plt

vV_0 = 1.38E3 # eV
vR_0 = 3.28E-1 # Angstrom
vK = 1.44E1 # eV * Angstrom

def fPotencial(x):
    return -(vK/(vV_0*vR_0))/x+math.exp(-x)

def fForca(x):
    return -(vK/(vV_0*vR_0))/(x**2)+math.exp(-x)

lRaio = []
lPotencial = []
lForca = []


for vR in np.arange(0.001, 10, 0.0005):

    lRaio.append(vR)
    lPotencial.append(fPotencial(vR))
    lForca.append(fForca(vR))


plt.plot(lRaio, lPotencial)
plt.title("$V(r)/V_0$ vs. $r/r_0$")
plt.xlabel("$r/r_0$")
plt.ylabel("$V(r)/V_0$")
plt.ylim(-0.005,0.005)
plt.xlim(0,10)
plt.grid()
plt.show()

plt.plot(lRaio,lForca)
plt.title("$r_0\cdot F(r)/V_0$ vs. $r/r_0$")
plt.xlabel("$r/r_0$")
plt.ylabel("$r_0\cdot F(r)/V_0$")
plt.ylim(-0.005,0.005)
plt.xlim(0,10)
plt.grid()
plt.show()