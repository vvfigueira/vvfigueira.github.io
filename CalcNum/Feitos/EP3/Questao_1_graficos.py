import matplotlib.pyplot as plt
from math import log

def Trunca(x):

    ex = (-6.01829e-1)*x + (2.18789e-1)

    return ex

def Round_simp16(x):

    ajuste = (3.81869e-1)*x + (-9.86099)

    return ajuste

def Round_simp8(x):

    ajuste = (7.01149e-2)*x + (-6.05982)

    return ajuste

def Round_dupl(x):

    ajuste = (3.44063e-2)*x + (-1.29958e1)

    return ajuste

erro_simples = [0.406250, 0.103516, 0.026001, 0.006508, 0.001628, 0.000408, 0.000102, 0.000027, 0.000012, 0.000003, 0.000004, 0.000007, 0.000003, 0.000004, 0.000003, 0.000094, 0.000277, 0.000484, 0.002491, 0.007617, 0.004385, 0.044366, 0.277420, 0.564703, 2.000000]
erro_dupla = [0.406250000000000, 0.103515625000000, 0.026000976562500, 0.006507873535156, 0.001627445220947, 0.000406891107559, 0.000101724639535, 0.000025431276299, 0.000006357826351, 0.000001589456852, 0.000000397364335, 0.000000099341072, 0.000000024835254, 0.000000006208840, 0.000000001552174, 0.000000000388059, 0.000000000096839, 0.000000000024241, 0.000000000005815, 0.000000000001452, 0.000000000000672, 0.000000000000703, 0.000000000000163, 0.000000000002173, 0.000000000000568]
p = []
Ajuste_Truncamento_simp = []
Ajuste_Truncamento_dupl = []
Ajuste_Roundoff_simp8 = []
Ajuste_Roundoff_simp16 = []
Ajuste_Roundoff_dupl = []
p_trunc_simp = []
p_trunc_dupl = []
p_round_simp8 = []
p_round_simp16 = []
p_round_dupl = []

for i in range(25):

    erro_simples[i] = log(erro_simples[i], 10)
    erro_dupla[i] = log(erro_dupla[i], 10)
    p.append(i+1)

    if i < 20:

        Ajuste_Truncamento_dupl.append(Trunca(i+1))
        p_trunc_dupl.append(i+1)

        if i < 8:

            Ajuste_Truncamento_simp.append(Trunca(i+1))
            p_trunc_simp.append(i+1)

        elif i < 16:

            Ajuste_Roundoff_simp8.append(Round_simp8(i+1))
            p_round_simp8.append(i+1)

        else:

            Ajuste_Roundoff_simp16.append(Round_simp16(i+1))
            p_round_simp16.append(i+1)

    else:

        Ajuste_Roundoff_simp16.append(Round_simp16(i+1))
        p_round_simp16.append(i+1)

        Ajuste_Roundoff_dupl.append(Round_dupl(i+1))
        p_round_dupl.append(i+1)

plt.plot(p,erro_simples,'o',label='Precisão Simples')
plt.plot(p,erro_dupla,'o',label='Precisão Dupla')
plt.plot(p_trunc_simp,Ajuste_Truncamento_simp,'--',label='Ajuste linear truncamento Trapezio simples')
plt.plot(p_trunc_dupl,Ajuste_Truncamento_dupl,'--',label='Ajuste linear truncamento Trapezio dupla')
plt.plot(p_round_simp8,Ajuste_Roundoff_simp8,'--',label='Ajuste linear no Roundoff simples')
#plt.plot(p_round_simp16,Ajuste_Roundoff_simp16,'--',label='Ajuste linear no Roundoff simples 2')
plt.plot(p_round_dupl,Ajuste_Roundoff_dupl,'--',label='Ajuste linear no Roundoff dupla')
plt.xlabel("p")
plt.ylabel("$\log_{10}(erro)$")
plt.title("Gráfico de erro")
plt.legend()
plt.show()
