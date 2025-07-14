from numpy import arange, empty
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def atualiza_linha(j, data, line):

    line.set_data(data[..., :j])
    return line,

#Tamanho do passo
h = 0.01

data = empty((2,4000),dtype=float)

#Condicao inicial de x
x0 = 1
v0 = -0.5

#Iniciamos nossas variaveis x e v pelos seus valores iniciais e a adicionamos
#as nossas listas
x = x0
v = v0

j = 0
#Implementamos o método de RK4 indo de t = 0 ate t = 5 a passos de h
for t in arange(0,40,h):

    data[0,j] = x
    data[1,j] = v

    #Para cada loop, calculamos o valor dos passos em x e v a serem tomados
    passo_x, passo_v = passo_RK4(t,x,v,h)

    #Atualizamos entao os valores de x e v a partir do passo calculado acima
    x = x + passo_x
    v = v + passo_v

    j += 1

#Ao fim do loop, plotamos o nosso diagrama de fases
fig = plt.figure()
plt.title("Diagramas de espaço de fase")
plt.xlabel("$x(t)$")
plt.ylabel("$\dot x(t)$") 
l, = plt.plot([],[], 'r-')
linha_ani = animation.FuncAnimation(fig, \
                                    atualiza_linha, \
                                    fargs=(data,1), \
                                    interval = 10, \
                                    blit = True)

plt.show()
