import math
import tabulate

vPrecisao = 1.E-10

def fNewton(x):
    return x - (x**(3/4) - math.cos(x**2))/((3/4)*(x**(-1/4)) + 2*x*math.sin(x**2))

def fZero(x):
    return x**(3/4) - math.cos(x**2)

def fZeroD(x):
    return (3/4)*(x**(-1/4)) + 2*x*math.sin(x**2)

def fErro(x):
    return abs((fNewton(x)-x)/x)

vInicial = 0.8

tDados = [["n","x_n","f(x_n)","f'(x_n)","Erro"]]

vIteracao = 0

while fErro(vInicial) > vPrecisao:
    
    tTemp = []
    tTemp.append(vIteracao)
    tTemp.append(round(vInicial,10))
    tTemp.append(fZero(vInicial))
    tTemp.append(fZeroD(vInicial))
    tTemp.append(fErro(vInicial))
    tDados.append(tTemp)
    
    vIteracao = vIteracao + 1
    vInicial = fNewton(vInicial)

tTemp = []
tTemp.append(vIteracao)
tTemp.append(format(vInicial))
tTemp.append(fZero(vInicial))
tTemp.append(fZeroD(vInicial))
tTemp.append(fErro(vInicial))
tDados.append(tTemp)

print("A raiz da função é: %.10f" %vInicial)
print()
print(tabulate.tabulate(tDados, headers='firstrow', tablefmt='latex'))