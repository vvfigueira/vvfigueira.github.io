from math import cos, sin
from tabulate import tabulate

#Precisao
epsilon = 1e-10

def f(x):

    f = x**3 - cos(x)

    return f

def df(x):

    df = 3*x**2 + sin(x)

    return df

def G(x):
    ''' Funcao que toma um valor de x_n e calcula o valor da funcao recursiva
        G(x_n) = x_n - f(x_n)/f'(x_n)
        = x_n - ((x_n)^3 - cos(x_n))/(3(x_n)^2 + sin(x_n))
        '''

    G = x - (x**3 - cos(x))/(3*x**2 + sin(x))

    return G

Dados = [["$n$","$x_n$","$f(x_n)$","$f'(x_n)$","$e_n$"]]
n = 0
x_n = 1 #Tomamos o valor inicial x_0 = 1
x_n_1 = G(x_n) #Calculamos o valor de x_{n+1} = x_1
print(x_n_1)

erro = abs((x_n_1 - x_n)/x_n) #Avaliamos o erro relativo entre x_0 e x_1

Primeiro = [n,x_n,f(x_n),df(x_n),erro]
Dados.append(Primeiro)

#Enquanto o erro for maior que a precisao, o programa continua
while erro > epsilon:

    Atual = []

    n = n + 1
    Atual.append(n)

    x_n = x_n_1 #Colocamos o valor anterior de x_{n+1} como o atual valor de x_n
    x_n_1 = G(x_n) #Recalculamos x_{n+1} a partir do novo x_n
    Atual.append(x_n)
    Atual.append(f(x_n))
    Atual.append(df(x_n))
    print(x_n_1)

    erro = abs((x_n_1 - x_n)/x_n) #Verificamos o erro relativo do passo atual
    Atual.append(erro)

    Dados.append(Atual)

#Saímos do loop com o valor desejado, e o printamos
print("A raiz de f(x) = x^3 - cos(x), com precisao de epsilon = 1e-10, eh de %.10f" %(x_n_1))
print()
print(tabulate(Dados, headers="firstrow", tablefmt="latex"))
