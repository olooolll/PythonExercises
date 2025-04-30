"""
Casamento de inteiros

Vamos definir a operação de casamento de dois números inteiros A e B da seguinte
forma:

inicialmente fazemos A e B terem o mesmo número de dígitos, adicionando zeros
à esquerda conforme necessário;
então cada dígito de A (do menos significativo ao mais significativo) é

comparado com o dígito correspondente de B, e o dígito de menor valor é
eliminado do número a que pertence (se os dígitos são iguais nenhum é
eliminado).

o resultado da operação de casamento é o par de números inteiros formados
pelos dígitos remanescentes de A e B. No caso de não haver digito remanescente
para um dos números, o resultado para esse número é -1.

Por exemplo, considere o casamento de 69961 com 487920:

O resultado do casamento é o par de números 489 e 9961. Dados dois números inteiros,
sua tarefa é determinar o resultado do casamento desses dois números.
Entrada

A primeira linha da entrada contém um número inteiro A, a segunda linha contém um
número inteiro B.

Saída

Seu programa deve produzir uma única linha, contendo os dois números inteiros
produzidos pelo casamento dos números dados, em ordem não decrescente.
Restrições

 1 ≤ A ≤ 109

 1 ≤ B ≤ 109

"""


userInputNumberA = int(input('Informe o primeiro número: '))
userInputNumberB = int(input('Informe o segundo número: '))
listNumberA = []
listNumberB = []

listResut = [[],[]]


if 1 <= userInputNumberA <= 10000000000 and 1 <= userInputNumberB <= 10000000000:
    stringNumeberA = str(userInputNumberA)
    stringNumeberB = str(userInputNumberB)

    if len(stringNumeberA) > len(stringNumeberB):
    
        i = 0
        while i < (len(stringNumeberA) - len(stringNumeberB)):
            listNumberB.append('0')
            i += 1
    
    elif len(stringNumeberA) < len(stringNumeberB):
    
        i = 0
        while i < (len(stringNumeberB) - len(stringNumeberA)):
            listNumberA.append('0')
            i += 1

    for char in stringNumeberA:
        listNumberA.append(char)

    for char in stringNumeberB:
        listNumberB.append(char)

    resutStringNumberA = ''
    resutStringNumberB = ''
    i = 0
    while i < len(listNumberA):
        if listNumberA[i] > listNumberB[i]:
            resutStringNumberA += listNumberA[i]
        
        elif listNumberA[i] < listNumberB[i]:
            resutStringNumberB += listNumberB[i]
        
        else:
            resutStringNumberA += listNumberA[i]
            resutStringNumberB += listNumberB[i]

        i += 1
            
    if not resutStringNumberA:
        resutStringNumberA = '-1'
    if not resutStringNumberB:
        resutStringNumberB = '-1'

    print(listNumberA)
    print(listNumberB)

    print(resutStringNumberB, resutStringNumberA)
    # for char in stringNumeberA:
    #     listNumberA.append(char)

else:
    print(f'Erro: 1 <= {userInputNumberA} <= 10000000000 e/ou 1 <= {userInputNumberB} <= 10000000000')