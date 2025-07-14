from math import sin, sqrt, pi

def k(theta_0):
    ''' Toma um valor de angulo inicial theta_0, em radianos, e determina a
        constante k = sin(theta_0/2) '''

    K = sin(theta_0/2)

    return K

def f(csi,k):
    ''' A partir de um ponto csi e uma constante k, determina o valor da
        funcao f(csi) = 1/sqrt(1 - k^2*sin^2(csi)) neste ponto '''

    func = 1/sqrt(1 - k**2 * sin(csi)**2)

    return func

def Simpson(K,a,b):
    ''' Dado uma constante de valor inicial K, um intervalo de integracao
        [a,b], realiza uma integracao numerica da funcao f(x) pelo metodo
        de Simpson, por meio da formula simplificada
        S = h/3[f_1 + f_n + 4*sum_{i pares} f_i + 2*sum_{i impares} f_i] '''

    #Iniciamos determinando o numero de intervalos N para realizar a integracao
    #e conjuntamente o tamanho do passo de integracao h
    N = 128
    h = (b - a)/N

    #Definimos o somatorio parcial ja calculando seus dois primeiros termos
    #nos extremos (f_1 e f_n)
    S = f(a,K) + f(b,K)

    #Iniciamos um loop para calcular os outros termos do somatorio indo de 1 a
    #N-1
    for i in range(1,N):

        #Calculamos a funcao f_{i+1} - Note que isso se faz necessario pois
        #i parte de 1, mas a nossa formula parte de i = 2
        termo = f(a + i*h, K)

        #Quando o valor de (i+1) for par, devemos multiplicar a funcao calculada
        #por 4, e quando for impar, devemos multiplica-lo por 2
        if i%2 != 0:

            S = S + 4*termo

        else:

            S = S + 2*termo

    #Apos somar todos os termos presentes nas chaves [] que determinam a
    #integral pelo metodo de Simpson, multiplicamos pela fator de h/3
    S = S*h/3

    return S

#Valores extremos do intervalo de integracao [a,b]
a = 0
b = pi/2

#Para calcular o periodo do pendulo necessitamos de valores para l e para g.
#l foi arbitrariamente tomado como l = 1 metro
l = 1
g = 9.8

#Definimos aqui uma variavel com o valor maximo tomado por theta_0 por
#conveniencia
theta = pi

#Devemos tomar 10 valores de theta_0 e portanto iniciamos um loop que se repete
#10 vezes
for i in range(10):

    #Escolhemos o valor do angulo inicial dividindo o intervalo [0,pi) em 10
    #intervalos igualmente espacados e tomamos cada um destes valores
    #individualmente
    theta_0 = (theta/10)*i

    #A partir de theta_0 determinamos a constante k
    K = k(theta_0)

    #Realizamos entao a integracao para o valor de theta_0 atual, e multiplicamos
    #a integral por 4*sqrt(l/g)
    T = 4*sqrt(l/g)*Simpson(K,a,b)

    #Tendo o valor do periodo, imprimimos os valores junto com o valor tomado
    #para theta_0
    print('theta_0 = %f, T = %f' %(theta_0,T))
