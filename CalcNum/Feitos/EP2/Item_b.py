def Escalona(A):
    ''' Recebe uma matriz aumentada A e por meio da Eliminacao por Gauss,
        utilizando pivotamento parcial, retorna a matriz triangular superior
        respectiva '''

    n = len(A) #Numero de linhas da matriz (igual ao tamanho da matriz quadrada
               #original)

    for k in range(n-1): #Varremos as n-1 primeiras colunas da matriz
                         #quadrada original para escalonar ela

        ######## Determinamos o indice do pivot l ########

        p = 0 #O pivot da k-esima coluna comeca igual a 0
        L = 0 #Armazenamos em qual linha esta o pivot

        #Para determinar o pivot, devemos checar o k-esimo elemento das linhas
        #k a n
        for l in range(k,n):

            #Se o elemento da l-esima linha da k-esima coluna for maior que p,
            #em modulo, ele se torna o novo p e guardamos em qual linha ele
            #se encontra
            if abs(A[l][k]) > p:

                p = A[l][k]
                L = l

        ##################################################
                
        ###### Trocamos a linhas k e L entre si ######

        #Copiamos quais sao os elementos de cada uma destas linhas
        Linha_k = A[k][:]
        Linha_l = A[L][:]

        #E entao trocamos eles entre si
        A[k] = Linha_l
        A[L] = Linha_k

        #Printamos a matriz apos o pivotamento
        print("Pivotamento:")
        for elem in range(n):
            print(A[elem])
        ##############################################

        #Tendo feito este processo inicial, comecamos a analisar linha
        #por linha (da (k+1)-esima linha a n-esima) e fazemos a operacao
        #Linha j = (Linha k)*(Multiplicador j) + Linha j para zerar a coluna
        #abaixo do pivot. Obs: Multiplicador j = -(elemento da j-esima
        #linha)/pivot

        for j in range(k+1,n):

            mult = -A[j][k]/p

            for i in range(k,n+1):

                A[j][i] = A[k][i]*mult + A[j][i]

            #Printamos a matriz apos realizar as somas e multiplicacoes
            #de cada linha
            print("Soma e multiplicacao:")
            for elem in range(n):
                print(A[elem])

    return A

def Backward(A):
    ''' Recebe uma matriz triangular superior aumentada e realiza uma
        substituicao para tras, de modo a nos retornar um vetor final,
        solucao do sistema '''

    n = len(A)
    Sol = []

    #Iniciamos com um vetor solucao de dimensao n e todos elementos iguais a 0
    for s in range(n):

        Sol.append(0)

    for i in range(n-1,-1,-1):

        #Iniciamos dividindo o valor que multiplica a variavel x_i
        #de modo a ficar com uma expressao do tipo:
        #x_i + a_(i+1)j x_(i+1)j + ... + a_nj x_j = b_i
        fator = 1/A[i][i]
        soma = 0

        #Fazemos a substituicao das variaveis ja conhecidas e a somamos entre si
        for j in range(i+1,n):

            soma = soma + Sol[j]*A[i][j]

        #Calculamos entao o valor de x_i que eh solucao de nosso problema
        Sol[i] = fator*(A[i][n] - soma)

    return Sol

#Iniciamos com uma matriz quadrada n x n A, um vetor resultante b e um vetor
#vazio x
A = [[0,5,-1],[13,0,1],[1,-1,-1]]
b = [4,15,0]
x = []

n = len(A)

#Transformamos nossa matriz A em uma matriz aumentada
for i in range(n):

    A[i].append(b[i])

#Por fim, escalonamos a matriz A (aumentada) e entao realizamos uma substituicao
#para tras para determinar o nosso vetor solucao x
A = Escalona(A)
x = Backward(A)

print("A solucao deste sistema eh dada por: I_1 = %f, I_2 = %f e I_3 = %f" %(x[0],x[1],x[2]))
