vPrecisao = 1.E-3

def fJacobi(tMatrix, tX0, tB):

    vPasso = 0
    vErro = 10
    tXPasso = tX0[:]
    vDimensao = len(tX0)

    print("Passo: ", vPasso)
    print("Erro: --")
    print("Solução neste passo: ", tXPasso)

    while vErro > vPrecisao:

        tXProxPasso = tXPasso[:]

        for vLinha in range(vDimensao):

            vSoma = 0

            for vColuna in range(vDimensao):

                if vColuna == vLinha:

                    continue

                vSoma = vSoma + tXProxPasso[vColuna] * tMatrix[vLinha][vColuna]

            vFator = 1 / tMatrix[vLinha][vLinha]
            tXPasso[vLinha] = vFator * (tB[vLinha] - vSoma)

        vErro = 0

        for vLinha in range(vDimensao):

            vErroTemp = abs(tXPasso[vLinha] - tXProxPasso[vLinha])

            if vErroTemp > vErro:

                vErro = vErroTemp

        vPasso = vPasso + 1

        print("Passo: ", vPasso)
        print("Erro: ", vErro)
        print("Solução neste passo: ", tXPasso)

    return(tXPasso)

tMatrix= [[11.9,0.0,1.8],[0.0,5.3,-1.8],[1,-1,-1]]
tB = [15.0,3.1,0]
tX0 = [0,0,0]

tSolucao = fJacobi(tMatrix, tX0, tB)

print("Solução Final: ", tSolucao)