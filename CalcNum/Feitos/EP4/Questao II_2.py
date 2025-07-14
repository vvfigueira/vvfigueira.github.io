from numpy import arange
from math import cos, pi
import matplotlib.pyplot as plt
from numba import njit

@njit
def f(t,x,v,F):
    ''' A partir dos atuais valores de t, x(t), v(t) e F calcula o valor
        de x''(t) '''

    f = 0.5*x*(1 - x**2) - 0.25*v + F*cos(omega*t)

    return f

@njit
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

#Valor da frequencia da forca
omega = 1

#Intervalo de intensidade de forca
DeltaF = 0.0005

#Condicoes iniciais
x0 = 1
v0 = -1

#Definimos os numeros de passos a serem tomados ate o fim do transiente e
#necessarios para completar um periodo
trans = 200000
periodo = 1000

#Listas para guardar os valores de x e F para construir o diagrama de bifurcacoes
X = []
F_list = []

#Realizamos entao um loop para todos os valores desejados para forca em
#intervalos igualmente espacados de DeltaF
for F in arange(0,0.7,DeltaF):

    #Para verificar o andamento do programa usamos um print para verificar
    #em qual valor de F estamos atualmente calculando (opcional)
    #print("F = %f" %F)

    #Iniciamos nossas variaveis x, v e t pelos seus valores iniciais
    t = 0
    x = x0
    v = v0

    #Definimos nossa precisao inicial
    h = 0.01*2*pi/omega

    #Evoluimos o sistema ate o fim do transiente
    t, x, v = RK4(t,x,v,F,h,trans)

    #Passado o transiente, reduzimos o tamanho do nosso passo h
    h = 0.001*pi/omega

    #Fazemos entao um loop para evoluir nosso sistema ao longo de 100 periodos
    for i in range(100):

        #Evoluimos nosso sistema em um periodo, dado por 1000 passos de RK4
        t, x, v = RK4(t,x,v,F,h,periodo)

        #Impressao dos valores de F e x atuais (opcional)
        #print("F = %f, x_i = %f" %(F,x))

        #Com os valores finais apos um periodo, guardamos estes valores em listas
        #para construir nosso diagrama
        X.append(x)
        F_list.append(F)

#Ao fim de todos os caluclos, plotamos o nosso diagrama de bifurcacao
plt.scatter(F_list,X,marker='.',s=.7)
plt.title("Diagrama de bifurcação")
plt.xlabel("$F$")
plt.ylabel("$x$")
plt.show()
