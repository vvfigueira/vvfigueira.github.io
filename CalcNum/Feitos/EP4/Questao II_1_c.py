from numpy import arange
from math import cos
import matplotlib.pyplot as plt

def f(t,x,v,F):
    ''' A partir dos atuais valores de t, x(t), v(t) e F calcula o valor
        de x''(t) '''

    f = 0.5*x*(1 - x**2) - 0.25*v + F*cos(omega*t)

    return f

def RK4(t,x,v,F,h,n):
    ''' Dado um valor de passos n, calcula a evolucao temporal de um sistema
        com valores iniciais de x, v, t, F dados, em n passos de Runge-Kutta,
        com uma precisao h, tambem dada'''

    #Tomamos um loop de n passos
    for i in range(n):

        #Fazemos entao os calculos referentes a um passo de RK4
        k1x = h*v
        k1v = h*f(t,x,v,F)
        k2x = h*(v+0.5*k1v)
        k2v = h*f(t+0.5*h,x+0.5*k1x,v+0.5*k1v,F)
        k3x = h*(v+0.5*k2v)
        k3v = h*f(t+0.5*h,x+0.5*k2x,v+0.5*k2v,F)
        k4x = h*(v+k3v)
        k4v = h*f(t+h,x+k3x,v+k3v,F)

        passo_x = (k1x+2*(k2x+k3x)+k4x)/6
        passo_v = (k1v+2*(k2v+k3v)+k4v)/6

        #Em seguida, sao atualizados os valores de x, v e t a partir dos
        #calculos acima
        x = x + passo_x
        v = v + passo_v
        t = t + h

    #Retornamos os valores finais de t, x e v apos os n passos de RK4
    return t, x, v

#Tamanho do passo
h = 0.01

#Condicao inicial de x
x0 = 1
v0 = -1
omega = 1

#Lista com os valores de forca a serem usados
fs = [0.22,0.23,0.28,0.35,0.6]

for F in fs:

    #Listas para guardar os valores de x e v para construir os diagramas de fases
    X = []
    V = []

    #Iniciamos nossas variaveis x e v pelos seus valores iniciais e a adicionamos
    #as nossas listas
    x = x0
    v = v0
    t = 0

    #Evoluimos nosso sistema em 200000 passos de RK4 para passarmos o transiente devido
    #ao amortecimento (equivalente a evoluir o sistema ate um t = 2000)
    t, x, v = RK4(t,x,v,F,h,200000)

    #Tendo passado o transiente, passamos a guardar as atualizacoes de x e v para podermos
    #montar nossos espacos de fases. Para isso usamos 15000 passos de RK4 (equivalente a
    #evoluir mais t = 150 unidades de tempo
    for i in range(15000):

        t, x, v = RK4(t,x,v,F,h,1)

        X.append(x)
        V.append(v)

    #Ao fim do loop, plotamos o nosso diagrama de fases
    plt.plot(X,V,label="$F = %.2f$" %F)
    plt.title("Diagramas de espaço de fase")
    plt.xlabel("$x(t)$")
    plt.ylabel("$\dot x(t)$")
    if F != 0.6:
        plt.ylim(-1.1,1.1)
        plt.xlim(-1.9,1.9)
    plt.grid()
    plt.legend()
    plt.show()
