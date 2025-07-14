from math import sin, sqrt, pi
import matplotlib.pyplot as plt

def k(theta_0):
    ''' Toma um valor de angulo inicial theta_0, em radianos, e determina a
        constante k = sin(theta_0/2) '''

    K = sin(theta_0/2)

    return K

def f(csi,k):
    ''' A partir de um ponto csi e uma constante k, determina o valor da
        funcao f(csi) = 1/sqrt(1 - k^2*sin^2(csi)) neste ponto '''

    func = 1/sqrt(1 - k**2 * sin(csi)**2)

    return func

def Simpson(K,a,b):
    ''' Dado uma constante de valor inicial K, um intervalo de integracao
        [a,b], e um numero de passos N, realiza uma integracao numerica da
        funcao f(x) pelo metodo de Simpson, por meio da formula simplificada
        S = h/3[f_1 + f_n + 4*sum_{i pares} f_i + 2*sum_{i impares} f_i] '''

    h = (b - a)/N
    S = f(a,K) + f(b,K)

    x_i = a

    for i in range(1,N):

        termo = f(x_i + i*h, K)

        if i%2 != 0:

            S = S + 4*termo

        else:

            S = S + 2*termo

    S = S*h/3

    return S

a = 0
b = pi/2
N = 256

theta = pi

T_Gal = 2*pi
T = []
Theta_0 = []

for i in range(100):

    theta_0 = (theta/100)*i
    Theta_0.append(theta_0)

    K = k(theta_0)

    t = 4*Simpson(K,a,b)
    T.append(t/T_Gal)

plt.plot(Theta_0,T)
plt.xlabel(r"$\theta_0$")
plt.ylabel("$T/T_{Galileu}$")
plt.title(r"Razão entre $T$ e $T_{Galileu}$ para valores arbitrarios de $\theta_0$")
plt.show()
