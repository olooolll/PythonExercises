"""
Faça um programa que leia uma quanƟdade N que indica o número de pessoas. Após
isso, leia a sequência de N alturas dessas pessoas e ao final mostre a sequência, a menor
altura e sua posição na sequência
"""

userInputIntN = int(input('Digite a o valor de N: '))
listOfAlt = []
i = 0
lessAlt = 9999999.99
indexlessAlt = 0

while i < userInputIntN:
    userInputAltFloat = float(input('Informe a altura: '))
    listOfAlt.append(userInputAltFloat)

    i += 1

print('Sequencia de altura: ')

i = 0
while i < userInputIntN:
    print(listOfAlt[i], end=', ')

    if listOfAlt[i] < lessAlt:
        lessAlt = listOfAlt[i]
        indexlessAlt = i
    
    i += 1
print()
print(f'A menor altura e sua posição na sequência: {lessAlt} | {indexlessAlt}')