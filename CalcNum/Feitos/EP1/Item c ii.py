from math import exp

#Constantes
K = 14.4 #eV*A - e^2/(4*pi*epsilon_0)
V_0 = 1.09e3 #eV
r_0 = 0.330 #A
epsilon = 1e-10

#Funcoes uteis
def F(r):
    ''' Para um dado valor de r, calcula o valor da forca entre dois ions de
        Na e Cl '''

    f = - K/(r**2) + (V_0/r_0)*exp(-r/r_0)

    return f

def G(r_n_1,r_n_2):
    '''Dado um valor de r_{n-1} e de r_{n-2}, eh calculado o proximo valor,
       r_{n}, a partir da formula de recursao dada atraves do metodo das
       secantes '''

    g = r_n_1 - F(r_n_1)*(r_n_1 - r_n_2)/(F(r_n_1) - F(r_n_2))

    return g

r_n_2 = 3 #r_0 = r_{n-2}
r_n_1 = 2.5 #r_1 = r_{n-1}

#r_2 = r_n = r_{n-1} - F(r_{n-1})*(r_{n-1} - r_{n-2})/(F(r_{n-1}) - F(r_{n-2}))
r_n = G(r_n_1,r_n_2)

e_n = abs((r_n - r_n_1)/r_n_1) #Erro relativo entre r_{n-1} e r_n

#Iremos realizar a integracao enquanto o erro relativo for maior que a
#precisao desejada
while e_n > epsilon:

    #Atualizamos as variaveis do loop anterior, para seus respectvos
    #valores pro loop atual. Isto eh: r_{n-2} -> r_{n-1} e
    #r_{n-1} -> r_n
    r_n_2 = r_n_1
    r_n_1 = r_n

    #Calculamos entao o novo valor de r_n da recursao
    r_n = G(r_n_1,r_n_2)

    #Atualizamos o valor do erro relativo
    e_n = abs((r_n - r_n_1)/r_n_1)

#Printamos o resultado obtido
print("O ponto de equilibrio r = r_eq, tal que F(r) = 0 e V(r) eh minimo")
print("eh dado por r_eq = %.10f A" %r_n)
