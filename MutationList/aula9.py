"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros e
os coloque em uma lista. Ao fim escreva os elementos da lista na ordem inversa
que foram lidos.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

lenListValuesInt = len(listValuesInt) - 1
i = -1

print('A ordem inversa que foram lidos: ', end='')
while i < lenListValuesInt:
    print(f'{listValuesInt[i]}', end=', ')
    i += 1