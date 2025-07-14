import math

vPrecisao = 1.E-6

def fZero(x):
    return x**(3/4) - math.cos(x**2)

def fBissecao( fZero, 
                   pInicial, 
                   pFinal):

    while abs(pInicial - pFinal) > vPrecisao:

        pMedio = (pInicial + pFinal)/2

        if ( (fZero(pInicial) * fZero(pMedio)) > 0 ):
            pInicial = pMedio
        else:
            pFinal = pMedio

    return pInicial

pRaiz = fBissecao(fZero, 0, 1)

print("A raiz da funcao é: %.6f" %pRaiz)