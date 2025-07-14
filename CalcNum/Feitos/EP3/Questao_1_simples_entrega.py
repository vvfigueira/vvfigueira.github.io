from numpy import float32

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

#Definimos o nosso numero de passos N
N = 2**10

#Realizamos a integral para N passos, indo de a ate b
Integral = float32(Trapezio(a,b,N))

#Printamos por fim o valor obtido da integral
print("A integral de 0 a 1 de f(x) = 7 - 5x^4, calculada pelo metodo de Trapezios em precisao simples, com %i passos de integracao eh dada por I = %f" %(N,Integral))
