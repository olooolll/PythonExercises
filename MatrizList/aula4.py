"""
Faça um programa que leia a ordem de uma matriz quadrada e gere a matriz
identidade correspondente. Mostre a matriz gerada em formato matricial.
"""

mat = []
index = 0

userInputRange = int(input('Informe o tamanho da matriz quadrada: '))

for i in range(userInputRange):
    mat.append([])
    for j in range(userInputRange):
        if j == index:
            mat[-1].append(1)
        else:
            mat[-1].append(0)
    index += 1

for i in mat: print(i)
