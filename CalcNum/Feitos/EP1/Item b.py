from math import cos, sin

#Precisao
epsilon = 1e-10

def G(x):
    ''' Funcao que toma um valor de x_n e calcula o valor da funcao recursiva
        G(x_n) = x_n - f(x_n)/f'(x_n)
        = x_n - ((x_n)^3 - cos(x_n))/(3(x_n)^2 + sin(x_n))
        '''

    G = x - (x**3 - cos(x))/(3*x**2 + sin(x))

    return G

x_n = 1 #Tomamos o valor inicial x_0 = 1
x_n_1 = G(x_n) #Calculamos o valor de x_{n+1} = x_1

erro = abs((x_n_1 - x_n)/x_n) #Avaliamos o erro relativo entre x_0 e x_1

#Enquanto o erro for maior que a precisao, o programa continua
while erro > epsilon:

    x_n = x_n_1 #Colocamos o valor anterior de x_{n+1} como o atual valor de x_n
    x_n_1 = G(x_n) #Recalculamos x_{n+1} a partir do novo x_n

    erro = abs((x_n_1 - x_n)/x_n) #Verificamos o erro relativo do passo atual

#Saimos do loop com o valor desejado, e o printamos
print("A raiz de f(x) = x^3 - cos(x), com precisao de epsilon = 1e-10, eh de %.10f" %(x_n_1))
