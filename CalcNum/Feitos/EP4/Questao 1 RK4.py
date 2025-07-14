from numpy import arange

def g(t,y,z):
    ''' A partir dos atuais valores de t, y(t) e y'(t) calcula o valor de
        y''(t) '''

    g = 12*t**2 + 4*t**3 - t**4 + y - z

    return g

def passo_RK4(t,y,z,h):
    ''' Dados os valores de t, y, z = y' e h, calcula pelo metodo de Runge-Kutta
        de 4a ordem, os valores de y(t+h) e z(t+h) '''

    k1y = h*z
    k1z = h*g(t,y,z)
    k2y = h*(z+0.5*k1z)
    k2z = h*g(t+0.5*h,y+0.5*k1y,z+0.5*k1z)
    k3y = h*(z+0.5*k2z)
    k3z = h*g(t+0.5*h,y+0.5*k2y,z+0.5*k2z)
    k4y = h*(z+k3z)
    k4z = h*g(t+h,y+k3y,z+k3z)

    passo_y = (k1y+2*(k2y+k3y)+k4y)/6
    passo_z = (k1z+2*(k2z+k3z)+k4z)/6

    return passo_y, passo_z

#Tamanho do passo
h = 0.01

#Condicoes iniciais
y0 = 0
z0 = 0

#Iniciamos nossas variaveis y e z pelos seus valores iniciais
y = y0
z = z0

#Implementamos o metodo de RK4 indo de t = 0 ate t = 5 a passos de h
for t in arange(0,5,h):

    #Para cada loop, calculamos o valor dos passos em y e z a serem tomados
    passo_y, passo_z = passo_RK4(t,y,z,h)

    #Atualizamos entao os valores de y e z a partir do passo calculado acima
    y = y + passo_y
    z = z + passo_z

#Printamos por fim os valores obtidos com 8 casas decimais para observar o ponto
#de variacao do resultado
print("y(5) = %.8f, z(5) = %.8f" %(y,z))
