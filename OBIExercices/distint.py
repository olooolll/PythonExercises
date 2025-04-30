"""
Você foi contratado pela Agência Extra-Espacial Brasileira, que procura indícios de vida extraterrestre.

Um dos telescópios da Agência, para o espectro ultravioleta, gera uma sequência de valores inteiros positivos que devem ser analisados diariamente. Sua primeira missão é determinar, na sequência gerada, o tamanho do maior intervalo contínuo que contém apenas números distintos.

Entrada

A primeira linha contém um inteiro 𝑁N, o número de elementos da sequência. Cada uma das linhas seguintes contém um inteiro Ii, os elementos da sequência na ordem em que foram gerados.

Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, o número de elementos do maior intervalo que contém apenas números distintos.

"""

actualList = []
mostLenList = len(actualList)

userInputQuantity = int(input('Informe a qunatidade de elementos: '))

for number in range(userInputQuantity):
    userInputNumber = input('Infor o número: ')
    
    if len(actualList) > mostLenList:
        mostLenList = len(actualList)

    if userInputNumber in actualList:
        actualList = []

    actualList.append(userInputNumber)
    print(actualList)

print(mostLenList)


