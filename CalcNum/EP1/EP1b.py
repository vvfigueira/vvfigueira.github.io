import math

vPrecisao = 1.E-10

def fNewton(x):
    return x - (x**(3/4) - math.cos(x**2))/((3/4)*(x**(-1/4)) + 2*x*math.sin(x**2))

def fErro(x):
    return abs((fNewton(x)-x)/x)

vInicial = 0.8

while fErro(vInicial) > vPrecisao:
    
    vInicial=fNewton(vInicial)

print("A raiz da função é: %.10f" %vInicial)