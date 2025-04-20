"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X. Ao fim escreva a posição na lista em que o
valor X foi encontrado. Se X não esƟver na lista, escrever -1.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

userInputXInt = int(input('Informe um número para verificar se está na lista: '))

lenListValuesInt = len(listValuesInt)
findNumberBoll = False
index = 0
i = 0
while i < lenListValuesInt:
    if listValuesInt[i] == userInputXInt:
        index = i
        findNumberBoll = True


    i += 1


if findNumberBoll:
    print(f'O número está na posição {index}')
else:
    print('-1')