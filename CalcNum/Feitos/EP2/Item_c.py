#Constantes
epsilon = 1e-4

#Funcoes a serem usadas
def Jacobi(A,x_0,b):
    '''Recebe uma matriz A_nxn, um vetor inicial x_0 e um vetor resultante b
       e resolve o sistema Ax = b a partir metodo de Jacobi para um criterio
       de parada max|x_i(k+1) - x_i(k)| < epsilon, e imprime o numero da iteracao
       k, junto com os valores de x_i e o erro referente a cada iteracao. Ao
       fim, retorna o vetor solucao'''

    #Iniciamos com um passo k = 0 e um erro arbitrariamente grande por nao
    #possuirmos um vetor x_{n-1}
    k = 0
    erro = 10
    x_k = x_0[:]
    n = len(x_0)

    #Imprimimos os primeiros valores para k, I_1, I_2, I_3. Pelo erro ter sido
    #escolhido arbitrariamente, nao o incluimos na listagem
    print("k = %i, I_1 = %f, I_2 = %f, I_3 = %f, erro = --" %(k,x_k[0],x_k[1],x_k[2]))

    #Realizaremos iteracoes ate que o erro seja menor que a precisao definida
    while erro > epsilon:

        #Ao comeco da iteracao, colocamos o vetor x_{k-1} como igual ao vetor
        #da iteracao anterior
        x_k_1 = x_k[:]

        #Fazemos o calculo para cada componente i do vetor x
        for i in range(n):

            #Utilizamos uma variavel para guardar os termos referentes ao
            #somatorio
            soma = 0

            for j in range(n):

                #Excluimos apenas do somatorio o termo quando i = j
                if j == i:

                    continue

                #Fazemos a soma em cima dos valores de x_{k-1}, calculados na
                #iteracao anterior
                soma = soma + x_k_1[j]*A[i][j]

            #Calculamos o fator que multiplica os termos entre parenteses
            #e entao determinamos o novo valor de x_i
            fator = 1/A[i][i]
            x_k[i] = fator*(b[i] - soma)

        #Tendo determinado os novos valores de x para esta iteracao,
        #calculamos o erro referente a ela
        erro = 0

        for i in range(n):

            er = x_k[i] - x_k_1[i]

            if er > erro:

                erro = er

        #Atualizamos o numero do passo
        k = k + 1

        #Imprimimos os valores desta iteracao de k, do vetor I e do erro
        print("k = %i, I_1 = %f, I_2 = %f, I_3 = %f, erro = %f" %(k,x_k[0],x_k[1],x_k[2],erro))

    return(x_k)

#Inserimos os valores de A, b e do chute inicial x_0
A = [[13,0,1],[0,5,-1],[1,-1,-1]]
b = [15,4,0]
x_0 = [1,1,1]

#Determinamos o vetor solucao a partir do metodo de Jacobi
x = Jacobi(A, x_0, b)

print("A solucao final eh dada por I_1 = %f, I_2 = %f, I_3 = %f" %(x[0],x[1],x[2]))
