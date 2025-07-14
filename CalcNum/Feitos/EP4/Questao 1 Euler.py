from numpy import arange

def g(t,y,z):
    ''' A partir dos atuais valores de t, y(t) e y'(t) calcula o valor de
        y''(t) '''

    g = 12*t**2 + 4*t**3 - t**4 + y - z

    return g

def passo_Euler(t,y,z,h):
    ''' Dados os valores de t, y, z = y' e h, calcula pelo metodo de Euler,
        os valores de y(t+h) e z(t+h) '''

    passo_y, passo_z = y + h*z, z + h*g(t,y,z)

    return passo_y, passo_z

#Condicoes iniciais
y0 = 0
z0 = 0

#Tamanho do passo
h = 0.01

#Iniciamos nossas variaveis y e z pelos seus valores iniciais
y = y0
z = z0

#Implementamos o metodo de Euler indo de t = 0 ate t = 5 a passos de h
for t in arange(0,5,h):

    #Para cada loop, atualizamos os valores de y e z
    y, z = passo_Euler(t,y,z,h)

#Printamos por fim os valores obtidos
print("y(5) = %f, z(5) = %f" %(y,z))
