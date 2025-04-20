"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores
inteiros. Em seguida leia um número inteiro X e remova todas as ocorrências desse
número da lista. Mostre a lista resultante.
○ A respeito de funções de lista, só é permiƟdo o uso da função append(), len() e del()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

userInputXValueInt = int(input('Informe o valor que deseja remover: '))

lenListValuesInt = len(listValuesInt)
i = 0
while i < lenListValuesInt:
    if listValuesInt[i] == userInputXValueInt:
        del listValuesInt[i]
        lenListValuesInt -= 1
    
    i += 1

print(listValuesInt)