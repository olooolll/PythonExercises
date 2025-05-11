"""
Faça um programa que leia 9 valores um a um e coloque em uma matriz 3x3. Após
isso, faça:
○ Imprima os 9 elementos no formato matricial
○ Imprima a soma total dos elementos
○ Imprima a soma dos elementos de cada linha
"""
mat = []

i = 0
while i < 9:
    if i % 3 == 0 or i == 0:
        mat.append([])
    
    userInputNumber = int(input('Informe um valor: '))
    mat[-1].append(userInputNumber)

    i += 1

sumMat = 0
for i in mat:
    
    print(i, end='')
    sumList = 0
    for j in i:
        sumList += j
    print(f' [{sumList}]')
    sumMat += sumList
print('\tTotal = ', sumMat)

