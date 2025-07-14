from math import sqrt

#Seed inicial Z_0 do nosso LCG, dada pelo meu numero USP
Z = 10819721

def random():
    ''' A partir de uma semente (seed) Z_0 = 10819721, definida globalmente,
        a funcao calcula o proximo numero Z segundo um LCG, alterando a variavel
        global, e por fim calcula o nosso numero 'aleatorio' no intervalo [0,1]
        pela divisao Z/m '''

    #Parametros do LCG
    a = 1103515245
    c = 12345
    m = 2147483647

    #Chamamos a nossa variavel global para podermos altera-la apos a chamada
    #da funcao
    global Z

    #Calculamos o valor Z_{i+1}
    Z = (a*Z+c)%m

    #Definimos o numero entre 0 e 1 dividindo Z por m
    U = Z/m

    return U

def f(x):
    ''' Dado um ponto x, calculamos o valor de y = x^4 '''

    y = x**4

    return y

def Monte_Carlo(N):
    ''' Dado um numero de pontos N, geramos N valores de x e N valores de y
        aleatoriamente, e entao avaliamos, pelo metodo de Monte Carlo, o valor
        da integral de 0 a 1 de f(x) '''

    #Comecamos com o numero de pontos embaixo da curva f(x) igual a zero
    MC = 0

    #Realizamos um loop do tamanho do numero de passos desejados
    for i in range(N):

        #Geramos dois numeros aleatorios x e y
        x = random()
        y = random()

        #Caso o valor de y esteja abaixo da funcao f(x), entao consideramos
        #este ponto para o nosso calculo, atualizando MC
        if y < f(x):

            MC = MC + 1

    #Apos obter todos os pontos abaixo de f(x), dividimos este numero pelo
    #numero total de pontos para obter o valor aproximado da integral
    I = MC/N

    return I

#Definimos quantos pontos desejamos
N = 100

for p in range(1,18):

    N_t = 2**p

    I_m = 0
    I_i = []

    for i in range(N_t):

        #Calculamos a integral pelo metodo de Monte Carlo para os N pontos
        I_i.append(Monte_Carlo(N))
            
        I_m = I_m + I_i[i]

    I_m = I_m/N_t

    sigma2 = 0

    for j in range(N_t):

        sigma2 = sigma2 + (I_i[j] - I_m)**2

    sigma2 = sigma2/(N_t - 1)
    sigma = sqrt(sigma2)

    sigma_m = sigma/sqrt(N_t)

    print("N_t: %i, I_m = %.15f, sigma = %.15f, sigma_m = %.15f" %(N_t, I_m, sigma, sigma_m))
