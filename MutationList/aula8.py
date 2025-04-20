"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Ao fim escreva o maior valor encontrado e sua posição na lista.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

lenListValuesInt = len(listValuesInt)
mostValueInt = listValuesInt[0]
index = 0
i = 0
while i < lenListValuesInt:
    if mostValueInt < listValuesInt[i]:
        index = i
        mostValueInt = listValuesInt[i]

    i += 1


print(f'O maior número {mostValueInt} está na posição {index}')
