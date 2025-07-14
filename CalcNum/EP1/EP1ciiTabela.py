import math
import tabulate

vV_0 = 1.38E3 # eV
vR_0 = 3.28E-1 # Angstrom
vK = 1.44E1 # eV * Angstrom

vPrecisao = 1E-10

def fPotencial(x):
    return -(vK/(vV_0*vR_0))/x+math.exp(-x)

def fForca(x):
    return -(vK/(vV_0*vR_0))/(x**2)+math.exp(-x)

def fSecante(vInicial, vFinal):
    return vFinal - fForca(vFinal)*(vFinal - vInicial)/(fForca(vFinal) - fForca(vInicial))

def fErro(vInicial, vFinal):
    return abs((fSecante(vInicial, vFinal) - vFinal)/vFinal)

vInicial = 6
vSegundo = 6.5

tDados = [["n","x_{n-1}","x_{n}", "x_{n+1}","f(x_n)","f(x_{n+1})","Erro"]]

vIteracao = 0

while fErro(vInicial, vSegundo) > vPrecisao:

    tTemp = []
    tTemp.append(vIteracao)
    tTemp.append(vInicial)
    tTemp.append(vSegundo)
    tTemp.append(fSecante(vInicial, vSegundo))
    tTemp.append(fForca(vSegundo))
    tTemp.append(fForca(fSecante(vInicial, vSegundo)))
    tTemp.append(fErro(vInicial, vSegundo))
    tDados.append(tTemp)

    vIteracao = vIteracao + 1

    vTemp = fSecante(vInicial, vSegundo)
    vInicial = vSegundo
    vSegundo = vTemp

tTemp = []
tTemp.append(vIteracao)
tTemp.append(vInicial)
tTemp.append(vSegundo)
tTemp.append(fSecante(vInicial, vSegundo))
tTemp.append(fForca(vSegundo))
tTemp.append(fForca(fSecante(vInicial, vSegundo)))
tTemp.append(fErro(vInicial, vSegundo))
tDados.append(tTemp)

tTemp = []
tTemp.append(vIteracao)
tTemp.append(":.10f".format(vInicial))
tTemp.append(":.10f".format(vInicial))
tTemp.append(":.10f".format(vInicial))
tTemp.append(fForca(vSegundo))
tTemp.append(fForca(fSecante(vInicial, vSegundo)))
tTemp.append(fErro(vInicial, vSegundo))
tDados.append(tTemp)

print("O raio de equilíbrio é r_eq/r_0 = %.10f" %vSegundo)
print()
print(tabulate.tabulate(tDados, headers='firstrow', tablefmt='latex'))