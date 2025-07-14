import math

vV_0 = 1.38E3 # eV
vR_0 = 3.28E-1 # Angstrom
vK = 1.44E1 # eV * Angstrom

vPrecisao = 1E-10

def fPotencial(x):
    return -(vK/(vV_0*vR_0))/x+math.exp(-x)

def fForca(x):
    return -(vK/(vV_0*vR_0))/(x**2)+math.exp(-x)

def fSecante(x, y):
    return y - fForca(y)*(y - x)/(fForca(y) - fForca(x))

def fErro(x, y):
    return abs((fSecante(x, y) - y)/y)

x = 1
y = 0.5

while fErro(x, y) > vPrecisao:

    a = fSecante(x, y)
    x = y
    y = a

print("O raio de equilíbrio é r_eq/r_0 = %.10f" %y)