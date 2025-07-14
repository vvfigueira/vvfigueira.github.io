def fTriangulacao(tMatrix):

    vDimensao = len(tMatrix) # Tamanho da matrix dada como input

    for vColuna in range(vDimensao-1):

        vPivot = 0 
        vLinhaPivot = 0 

        for vLinha in range(vColuna, vDimensao):

            if abs( tMatrix[vLinha][vColuna] ) > abs( vPivot ):

                vPivot = tMatrix[vLinha][vColuna]
                vLinhaPivot = vLinha

        vTemp1 = tMatrix[vColuna][:]
        vTemp2 = tMatrix[vLinhaPivot][:]

        tMatrix[vColuna] = vTemp2
        tMatrix[vLinhaPivot] = vTemp1

        print("Pivotamento:")
        print(tMatrix)

        for vLinha in range(vColuna + 1, vDimensao):

            vMlc = -tMatrix[vLinha][vColuna] / tMatrix[vColuna][vColuna]

            for vTempCol in range(vColuna, vDimensao + 1):

                tMatrix[vLinha][vTempCol] = tMatrix[vColuna][vTempCol] * vMlc + tMatrix[vLinha][vTempCol]

            print("Introdução de zeros abaixo do pivô:")
            print(tMatrix)

    return tMatrix

def fSolucionar(tMatrix):

    vDimensao = len(tMatrix)
    tSolucao = []

    for vLinhaTemp in range(vDimensao):

        tSolucao.append(0)

    for vLinha in range(vDimensao-1, -1, -1):

        vFator = 1 / tMatrix[vLinha][vLinha]
        vSoma = 0

        for vColuna in range(vLinha+1, vDimensao):

            vSoma = vSoma + tSolucao[vColuna] * tMatrix[vLinha][vColuna]

        tSolucao[vLinha] = vFator * (tMatrix[vLinha][vDimensao] - vSoma)

    return tSolucao

tMatrix = [[0.0,5.3,-1.8],[11.9,0.0,1.8],[1,-1,-1]]
tB = [3.1,15.0,0]
tX = []

vDimensao = len(tMatrix)

for vLinha in range(vDimensao):

    tMatrix[vLinha].append(tB[vLinha])


tMatrix = fTriangulacao(tMatrix)

print("Matrix Triangulada:")
print(tMatrix)

tX = fSolucionar(tMatrix)

print("Solução Final:")
print(tX)