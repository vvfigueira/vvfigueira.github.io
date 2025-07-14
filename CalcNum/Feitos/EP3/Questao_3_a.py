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
