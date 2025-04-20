"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores
inteiros. Ao fim escreva qual número aparece mais vezes na lista, considerando a
possibilidade de empate.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""

userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

largeocOrrencNumberInt = 0
for i in listValuesInt:

    ocorrencNumberInt = 0
    for j in listValuesInt:
        if i == j:
            ocorrencNumberInt += 1

    if ocorrencNumberInt > largeocOrrencNumberInt:
        largeocOrrencNumberInt = ocorrencNumberInt

largeocOrrencNumberList = []

lastNumber = None
for i  in listValuesInt:
    actualNumberOcorrencInt = 0
    for j in listValuesInt:
        if i == j:
            actualNumberOcorrencInt += 1
    
    if actualNumberOcorrencInt == largeocOrrencNumberInt and i != lastNumber:
        largeocOrrencNumberList.append(i)
    lastNumber = i

print(f'O(s) número(s) que aparce mais vezes é {largeocOrrencNumberList}')