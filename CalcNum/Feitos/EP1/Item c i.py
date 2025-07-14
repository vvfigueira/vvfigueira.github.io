from math import exp
from numpy import arange
import matplotlib.pyplot as plt

#Constantes
K = 14.4 #eV*A - e^2/(4*pi*epsilon_0)
V_0 = 1.09e3 #eV
r_0 = 0.330 #A

#Funcoes uteis
def V(r):
    ''' Para um dado valor de r, calcula o valor do potencial entre dois ions
        de Na e Cl '''

    v = - K/r + V_0*exp(-r/r_0)

    return v

def F(r):
    ''' Para um dado valor de r, calcula o valor da forca entre dois ions de
        Na e Cl '''

    f = - K/(r**2) + (V_0/r_0)*exp(-r/r_0)

    return f

#Inicio do programa
#Criacao das listas para r, V e F
r_lista = []
V_lista = []
F_lista = []

#Varremos valores de r desde 0.001 ate 50 em passos de 0.001
for r in arange(0.001,50,0.001):

    #Adicionamos o valor atual de r para a nossa lista
    r_lista.append(r)

    #Utilizando o valor de r atual, eh calculado o valor do potencial e entao
    #guardamos esse valor em nossa lista referente ao potencial
    V_var = V(r)
    V_lista.append(V_var)

    #Utilizando o valor de r atual, eh calculado o valor da forca e entao
    #guardamos esse valor em nossa lista referente a forca
    F_var = F(r)
    F_lista.append(F_var)

#Tendo as tres listas completas, plotamos os graficos do potencial e da forca
#separadamente, ajustando o intervalo de visualizacao adequado para cada caso
#e colocando uma grade para auxiliar a visualizacao
plt.plot(r_lista,V_lista)
plt.title("V(r) x r")
plt.xlabel("r ($\AA$)")
plt.ylabel("V(r) (eV)")
plt.ylim(-6,6)
plt.grid()
plt.show()

plt.plot(r_lista,F_lista)
plt.title("F(r) x r")
plt.xlabel("r ($\AA$)")
plt.ylabel("F(r) (eV/$\AA$)")
plt.ylim(-2,2)
plt.grid()
plt.show()