from math import exp
from tabulate import tabulate

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

Dados = []
Primeira = ["n","r_n-1","r_n","F(r_n-1)","F(r_n)","e_n"]
Segunda = [0,"",3,"",F(3),""]

Dados.append(Primeira)
Dados.append(Segunda)

e_1 = abs((2.5-3)/3)

Terceira = [1,3,2.5,F(3),F(2.5),e_1]
Dados.append(Terceira)

r_n_2 = 3 #r_0 = r_{n-2}
r_n_1 = 2.5 #r_1 = r_{n-1}

#r_2 = r_n = r_{n-1} - F(r_{n-1})*(r_{n-1} - r_{n-2})/(F(r_{n-1}) - F(r_{n-2}))
r_n = G(r_n_1,r_n_2)

e_n = abs((r_n - r_n_1)/r_n_1) #Erro relativo entre r_{n-1} e r_n

n = 2

Final = [n,r_n_1,r_n,F(r_n_1),F(r_n),e_n]
Dados.append(Final)

#Iremos realizar a integracao enquanto o erro relativo for maior que a
#precisao desejada
while e_n > epsilon:

    Atual = []

    n = n + 1
    Atual.append(n)

    #Atualizamos as variaveis do loop anterior, para seus respectvos
    #valores pro loop atual. Isto eh: r_{n-2} -> r_{n-1} e
    #r_{n-1} -> r_n
    r_n_2 = r_n_1
    r_n_1 = r_n
    Atual.append(r_n_1)

    #Calculamos entao o novo valor de r_n da recursao
    r_n = G(r_n_1,r_n_2)
    Atual.append(r_n)
    Atual.append(F(r_n_1))
    Atual.append(F(r_n))

    #Atualizamos o valor do erro relativo
    e_n = abs((r_n - r_n_1)/r_n_1)
    Atual.append(e_n)

    Dados.append(Atual)

    print("n: %s, r_{n-1} = %.10f, r_n = %.10f, F(r_{n-1}) = %.10f, F(r_n) = %.10f, e_n = %.10f" %(n,r_n_1, r_n, F(r_n_1), F(r_n), e_n))

#Printamos o resultado obtido
print()
print("O ponto de equilibrio r = r_eq, tal que F(r) = 0 e V(r) eh minimo")
print("eh dado por r_eq = %.10f A" %r_n)
print()
print(tabulate(Dados, headers="firstrow", tablefmt="latex"))
