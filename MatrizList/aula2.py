"""
Faça um programa que crie uma matriz MxM quadrada com números fornecidos
pelo usuário. Após isso imprima a diagonal principal dessa matriz e o valor de seu
traço.
"""

matriz = []

userInput = int(input('Informe o numero da matriz MxM: '))

for i in range(userInput):
    matriz.append([])
    for j in range(userInput):

        userInputNumber = int(input('Informe um número: '))
        matriz[-1].append(userInputNumber)

for i in matriz: 
    print(i)

sumMatrizSecun = 0
sumMatrizPrinc = 0

j = 0
h = -1
for i in matriz:
    sumMatrizSecun += i[j]
    sumMatrizPrinc += i[h]

    j += 1
    h += 1


print(sumMatrizPrinc, sumMatrizSecun)