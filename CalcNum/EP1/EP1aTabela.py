import math
import tabulate

vPrecisao = 1.E-6

def fZero(x):
    return x**(3/4) - math.cos(x**2)

def fTabDados(vIteracao, vInicial, vFinal, vMedio, fZero):

    tTemp = []
    tTemp.append(vIteracao)
    tTemp.append(vInicial)
    tTemp.append(vFinal)
    tTemp.append(vMedio)
    tTemp.append(fZero(vInicial))
    tTemp.append(fZero(vFinal))
    tTemp.append(vFinal-vInicial)
    
    return tTemp

def MetodoBissecao( fZero, 
                   vInicial, 
                   vFinal):
    
    tDados = [["n","x_0","x_1","x_m","f(x_0)","f(x_1)","Erro"]]

    vIteracao = 0

    while abs(vInicial - vFinal) > vPrecisao:

        vMedio = (vInicial + vFinal)/2

        tDados.append(fTabDados(vIteracao, vInicial, vFinal, vMedio, fZero))

        vIteracao = vIteracao + 1

        if ( (fZero(vInicial) * fZero(vMedio)) > 0 ):
            vInicial = vMedio
        else:
            vFinal = vMedio
    
    tDados.append(fTabDados(vIteracao, vInicial, vFinal, vMedio, fZero))

    return vInicial, tDados

pRaiz, tDados = MetodoBissecao(fZero, 0, 1)

print("A raiz da função é: %.6f" %pRaiz)
print()
print(tabulate.tabulate(tDados, headers='firstrow', tablefmt='latex'))