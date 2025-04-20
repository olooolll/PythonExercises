"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores
inteiros. Em seguida leia um número inteiro X. Ao fim escreva o número de vezes
que o número X aparece na lista.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

userInputXInt = int(input('Informe o valor que deseja procurar: '))

findNumberBoll = False
countFindNumbersInt = 0
for i in listValuesInt:
    if i == userInputXInt:
        findNumberBoll = True
        countFindNumbersInt += 1

print(f'número de vezes que o número {userInputXInt} aparece {countFindNumbersInt}x na lista')