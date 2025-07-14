from numpy import arange
import matplotlib.pyplot as plt

def f(t,x):
    ''' A partir dos atuais valores de t e x(t) calcula o valor de
        x''(t) '''

    f = 0.5*x*(1 - x**2)

    return f

def passo_RK4(t,x,v,h):
    ''' Dados os valores de t, x, v = x' e h, calcula pelo metodo de Runge-Kutta
        de 4a ordem, os valores de x(t+h) e v(t+h) '''

    k1x = h*v
    k1v = h*f(t,x)
    k2x = h*(v+0.5*k1v)
    k2v = h*f(t+0.5*h,x+0.5*k1x)
    k3x = h*(v+0.5*k2v)
    k3v = h*f(t+0.5*h,x+0.5*k2x)
    k4x = h*(v+k3v)
    k4v = h*f(t+h,x+k3x)

    passo_x = (k1x+2*(k2x+k3x)+k4x)/6
    passo_v = (k1v+2*(k2v+k3v)+k4v)/6

    return passo_x, passo_v

#Tamanho do passo
h = 0.01

#Condicao inicial de x
x0 = 1

for i in range(3):

    #Listas para guardar os valores de x e v para construir os diagramas de fases
    X = []
    V = []

    #Condicoes iniciais de v para cada tentativa
    if i == 0:

        v0 = -0.1

    elif i == 1:

        v0 = -0.5

    else:

        v0 = -1

    #Iniciamos nossas variaveis x e v pelos seus valores iniciais e a adicionamos
    #as nossas listas
    x = x0
    v = v0

    X.append(x)
    V.append(v)

    #Implementamos o método de RK4 indo de t = 0 ate t = 5 a passos de h
    for t in arange(0,40,h):

        #Para cada loop, calculamos o valor dos passos em x e v a serem tomados
        passo_x, passo_v = passo_RK4(t,x,v,h)

        #Atualizamos entao os valores de x e v a partir do passo calculado acima
        x = x + passo_x
        v = v + passo_v

        #Adicionamos os novos valores de x e v as listas X e V
        X.append(x)
        V.append(v)

    #Ao fim do loop, plotamos o nosso diagrama de fases
    plt.plot(X,V,label="$\dot x(0) = %.1f$" %v0)

plt.title("Diagramas de espaço de fase")
plt.xlabel("$x(t)$")
plt.ylabel("$\dot x(t)$")
#plt.ylim(-1.1,1.1)
#plt.xlim(-1.9,1.9)
plt.legend()
plt.show()
