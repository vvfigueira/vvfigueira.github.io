from numpy import float32

#Constantes
Exata = float32(6) #Valor exato da integral, calculado analiticamente

#Funcoes uteis
def f(x):
    ''' Funcao utilizada para calcular o valor do integrando em um ponto
        arbitrario x em precisao simples'''

    integ = float32(7 - 5*x**4)

    return integ

def Trapezio(a,b,N):
    ''' A partir de um numero de intervalos N e um intervalo de integracao
        [a,b], realiza uma integracao numerica da funcao f(x) pelo
        metodo de trapezios em precisao simples de a ate b em passos de
        tamanho h = 1/N'''

    #Iniciamos tomando o valor de cada passo h = 1/N e o valor inicial do
    #somatorio da integral = 0
    h = float32(1/N)
    T = float32(0)

    #Setamos o valor inicial de x_{i+1} como o inicio do nosso intervalo [a,b]
    x_i_1 = float32(a)

    #Eh iniciado entao um loop de N passos para realizar a integracao numerica
    for i in range(N):

        #Colocamos os valores de x_i e x_{i+1}, onde x_i toma o valor anterior
        #de x_{i+1}, e x_{i+1} toma o proximo valor de x = x_i + h (o valor
        #de x_i mais o tamanho do passo)
        x_i = float32(x_i_1)
        x_i_1 = float32(x_i + h)

        #Calculamos entao o novo termo da somatoria e entao o adicionamos ao
        #nosso valor total da integral
        termo = float32(h*((f(x_i) + f(x_i_1))/2))
        T = float32(T + termo)

    return T

#Valores extremos do intervalo [a,b] de integracao
a = 0
b = 1

#Nosso programa eh iniciado fazendo um loop pra cada p desejado, indo de 1 a 25
for p in range(1,26):

    #A partir de p definimos o nosso numero de passos N
    N = 2**p

    #Realizamos a integral para N passos, indo de a ate b
    Integral = float32(Trapezio(a,b,N))

    #Calculamos o erro da integral calculada em relacao ao valor exato da
    #integral, calculada analiticamente
    erro = float32(abs(Integral - Exata))

    #Por fim, printamos os valores de p, N, o valor calculado numericamente
    #para a integral e o seu erro
    print('p: %i, N: %i, I_num: %f, erro: %f' %(p,N,Integral,erro))
