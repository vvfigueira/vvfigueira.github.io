from numpy import float64

#Constantes
Exata = float64(6) #Valor exato da integral, calculado analiticamente

#Funcoes uteis
def f(x):
    ''' Funcao utilizada para calcular o valor do integrando em um ponto
        arbitrario x em precisao simples'''

    integ = float64(7 - 5*x**4)

    return integ

def Trapezio(a,b,N):
    ''' A partir de um numero de intervalos N e um intervalo de integracao
        [a,b], realiza uma integracao numerica da funcao f(x) pelo
        metodo de trapezios em precisao simples de a ate b em passos de
        tamanho h = 1/N'''

    #Iniciamos tomando o valor de cada passo h = 1/N e o valor inicial do
    #somatorio da integral = 0
    h = float64(1/N)
    T = float64(0)

    #Setamos o valor inicial de x_{i+1} como o inicio do nosso intervalo [a,b]
    x_i_1 = float64(a)

    #Eh iniciado entao um loop de N passos para realizar a integracao numerica
    for i in range(N):

        #Colocamos os valores de x_i e x_{i+1}, onde x_i toma o valor anterior
        #de x_{i+1}, e x_{i+1} toma o proximo valor de x = x_i + h (o valor
        #de x_i mais o tamanho do passo)
        x_i = float64(x_i_1)
        x_i_1 = float64(x_i + h)

        #Calculamos entao o novo termo da somatoria e entao o adicionamos ao
        #nosso valor total da integral
        termo = float64(h*((f(x_i) + f(x_i_1))/2))
        T = float64(T + termo)

    return T

#Nosso programa eh iniciado fazendo um loop pra cada p desejado, indo de 1 a 25
for p in range(1,26):

    #A partir de p definimos o nosso numero de passos N
    N = 2**p

    #Valores extremos do intervalo [a,b] de integracao
    a = 0
    b = 1

    #Realizamos a integral para N passos, indo de a ate b
    Integral = float64(Trapezio(a,b,N))

    #Calculamos o erro da integral calculada em relacao ao valor exato da
    #integral, calculada analiticamente
    erro = float64(abs(Integral - Exata))

    #Por fim, printamos os valores de p, N, o valor calculado numericamente
    #para a integral e o seu erro
    print('p: %i, N: %i, I_num: %.15f, erro: %.15f' %(p,N,Integral,erro))
