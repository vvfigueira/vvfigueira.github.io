from math import cos
from tabulate import tabulate

#Definicao de constantes
epsilon = 0.000001

#Construcao de funcoes
def f(x):
    ''' Funcao que toma um valor de x e calcula o valor da funcao
        f(x) = x^3 - cos(x) neste ponto '''

    f = x**3 - cos(x)

    return f

def bisec(f,a,b):
    ''' A partir de um dado intervalo [a,b] e uma funcao f(x), eh calculada
        a raiz de f(x) a partir do metodo da bisseccao '''

    Dados = [["$x_1$","$x_2$","$x_m$","$f(x_1)$","$f(x_m)$","e_n"]]

    #O intervalo comeca indo de a ate b
    x_1 = a
    x_2 = b


    #Realizamos um loop ate que o tamanho do intervalo seja menor que a precisao
    #desejada
    while abs(x_2 - x_1) > epsilon:

        Atual = []

        #Eh calculado o ponto medio entre x_1 e x_2
        x_m = (x_1 + x_2)/2

        #Calculamos o valor de e_n e incluimos os valores de interesse nas listas
        #de x_1, x_2 e e_n
        e_n = x_2 - x_1
        Atual.append(x_1)
        Atual.append(x_2)

        #Calculamos o valor de f nos pontos x_1 e x_m e incluimos eles, junto
        #com o valor de x_m em suas respectivas listas
        f_x_1 = f(x_1)
        f_x_m = f(x_m)
        Atual.append(x_m)
        Atual.append(f_x_1)
        Atual.append(f_x_m)
        Atual.append(e_n)

        Dados.append(Atual)

        #Se a funcao calculada nos pontos x_1 e x_m tiverem o mesmo sinal,
        #entao o seu produto sera positivo, e o intervalo passa a ser
        #[x_1,x_2] -> [x_m,x_2]
        if f(x_1)*f(x_m) > 0:

            x_1 = x_m

        #Caso o produto das duas seja negativo, entao elas possuem sinal diferente
        #e o intervalo eh atualizado para [x_1,x_2] -> [x_1,x_m]
        else:

            x_2 = x_m

    #Ao fim do loop, tomamos o valor de x_1 como sendo o valor da raiz de f(x)
    return x_1, Dados

#Inicio do programa
#Eh escolhido o intervalo de [-2,2]
x_a = -2
x_b = 2

Dados = []

#A raiz x_0 da funcao eh calculado usando o algoritmo de bisseccao
x_0, Dados = bisec(f,x_a,x_b)

#Tendo o valor de x_0, imprimimos ele
print("A raiz, x_0, da funcao eh: %.6f" %x_0)
print()
print(tabulate(Dados, headers="firstrow", tablefmt="latex"))
