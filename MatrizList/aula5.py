"""
Faça um programa que leia duas matrizes de mesma ordem MxN e mostre as duas
matrizes originais e a matriz resultante da soma dessas matrizes, em formato
matricial.
"""
mat1 = []
mat2 = []

userInputRange = int(input('Informe o tamanho da matriz: '))

for i in range(userInputRange):
    mat1.append([])

    for j in range(userInputRange):
        userInputNumber = int(input('Informe o valor na matriz 1: '))
        mat1[-1].append(userInputNumber)
        
for i in range(userInputRange):
    mat2.append([])

    for j in range(userInputRange):
        userInputNumber = int(input('Informe o valor na matriz 2: '))
        mat2[-1].append(userInputNumber)

resultMat = []

for i in range(userInputRange):
    resultMat.append([])
    for j in range(userInputRange):
        resultMat[-1].append((mat1[i][j] + mat2[i][j]))

for i in range(userInputRange): print(f"{mat1[i]} + {mat2[i]} = {resultMat[i]}")