import matplotlib.pyplot as plt

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

def Monte_Carlo(N,visu_in,visu_out):
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
            visu_in.append([x,y])

        else:

            visu_out.append([x,y])

    #Apos obter todos os pontos abaixo de f(x), dividimos este numero pelo
    #numero total de pontos para obter o valor aproximado da integral
    I = MC/N

    return I

#Definimos quantos pontos desejamos
N = 100
h = 1/N

visu_in = []
visu_out = []

Exata = []
X = []

for i in range(N+1):
    Exata.append(f(h*i))
    X.append(h*i)

#Calculamos a integral pelo metodo de Monte Carlo para os N pontos
I = Monte_Carlo(N,visu_in,visu_out)

Visu_X_in = []
Visu_Y_in = []
Visu_X_out = []
Visu_Y_out = []

for j in range(len(visu_in)):

    Visu_X_in.append(visu_in[j][0])
    Visu_Y_in.append(visu_in[j][1])

for k in range(len(visu_out)):

    Visu_X_out.append(visu_out[k][0])
    Visu_Y_out.append(visu_out[k][1])

#Printamos o valor obtido
print("Utilizando %i pontos, calculamos pelo metodo de Monte Carlo a integral de f(x) = x^4 de 0 a 1 como sendo, aproximadamente %f" %(N,I))

print("Pontos dentro = %i" %len(visu_in))

plt.scatter(Visu_X_in,Visu_Y_in)
plt.scatter(Visu_X_out,Visu_Y_out)
plt.plot(X,Exata,label='$y = x^4$')
plt.legend(loc='upper right')
plt.title("Visualização do método de Monte Carlo")
plt.show()
