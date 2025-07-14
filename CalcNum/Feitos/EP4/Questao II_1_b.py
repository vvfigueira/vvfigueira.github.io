from numpy import arange
import matplotlib.pyplot as plt

def f(t,x,v,Gamma):
    ''' A partir dos atuais valores de t, x(t), v(t) e Gamma = 2*gamma calcula
        o valor de x''(t) '''

    f = 0.5*x*(1 - x**2) - Gamma*v

    return f

def passo_RK4(t,x,v,Gamma,h):
    ''' Dados os valores de t, x, v = x', Gamma e h, calcula pelo metodo de
        Runge-Kutta de 4a ordem, os valores de x(t+h) e v(t+h) '''

    k1x = h*v
    k1v = h*f(t,x,v,Gamma)
    k2x = h*(v+0.5*k1v)
    k2v = h*f(t+0.5*h,x+0.5*k1x,v+0.5*k1v,Gamma)
    k3x = h*(v+0.5*k2v)
    k3v = h*f(t+0.5*h,x+0.5*k2x,v+0.5*k2v,Gamma)
    k4x = h*(v+k3v)
    k4v = h*f(t+h,x+k3x,v+k3v,Gamma)

    passo_x = (k1x+2*(k2x+k3x)+k4x)/6
    passo_v = (k1v+2*(k2v+k3v)+k4v)/6

    return passo_x, passo_v

#Tamanho do passo
h = 0.01

#Condicao inicial de x
x0 = 1
v0 = -1

Gammas = [0.25,0.8]

for Gamma in Gammas:

    #Listas para guardar os valores de x e v para construir os diagramas de fases
    X = []
    V = []

    #Iniciamos nossas variaveis x e v pelos seus valores iniciais e a adicionamos
    #as nossas listas
    x = x0
    v = v0

    X.append(x)
    V.append(v)

    #Implementamos o método de RK4 indo de t = 0 ate t = 5 a passos de h
    for t in arange(0,40,h):

        #Para cada loop, calculamos o valor dos passos em x e v a serem tomados
        passo_x, passo_v = passo_RK4(t,x,v,Gamma,h)

        #Atualizamos entao os valores de x e v a partir do passo calculado acima
        x = x + passo_x
        v = v + passo_v

        #Adicionamos os novos valores de x e v as listas X e V
        X.append(x)
        V.append(v)

    #Ao fim do loop, plotamos o nosso diagrama de fases
    plt.plot(X,V,label="$2 \gamma = %.2f$" %Gamma)

plt.title("Diagramas de espaço de fase")
plt.xlabel("$x(t)$")
plt.ylabel("$\dot x(t)$")
plt.ylim(-1.1,1.1)
plt.xlim(-1.9,1.9)
plt.legend()
plt.show()
