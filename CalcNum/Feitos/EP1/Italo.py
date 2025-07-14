#Bibliotecas a serem utilizadas:
import numpy as np
import matplotlib.pyplot as plt

#QUESTÃO A: 
def bissecção(): #Define-se a fução algorítmica do método da bissecção:
    a = -1.0 #Extremo esquerdo do intervalo
    b = 2.0 #Extremo direito do intervalo
    p = 10**-6 #Precisão
    n = 0 #Número de interações

      
    if (f(a) * f(b) < 0): #Condição para que a raiz esteja no intervalo dado
        while(abs(a - b) > p):
            xm = (a + b) / 2 #Define-se a média
            fm = f(xm)
            if (f(xm) * f(a) > 0):
                a = xm
                fm = f(a)
            else:
                b = xm
                fm = f(b)
            e = abs(b-a)
            n = n + 1
        print("A raiz de f(x) é aproximadamente ", round(xm, 4) )
    else:
        print("Não há raiz no intervalo dado")
        
def f(x): #Define-se a fução da qual se obetrá a raiz:
    return ((x**3) - np.cos(x))

bissecção()
