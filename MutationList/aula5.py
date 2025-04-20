"""
Faça um programa que efetue a leitura de 15 elementos inteiros para uma lista
A. No final, apresente o total da soma de todos os elementos ímpares e pares.
Exemplos de entrada e saída:
"""
aList = []
sumParInt = 0
sumImpInt = 0

i = 0
while i < 15:
    userInputInt = int(input('Digite elementos inteiros: '))
    aList.append(userInputInt)

    if userInputInt % 2 == 0:
        sumParInt += userInputInt
    else:
        sumImpInt += userInputInt

    i += 1


print(f'Soma dos ímpares: {sumImpInt}')
print(f'Soma dos pares: {sumParInt}')

# ListaA: 7 -21 45 1 77 -5 98 3 55 31 2 10 4 1 9 