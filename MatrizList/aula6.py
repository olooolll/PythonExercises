"""
Faça um programa que leia uma matriz de ordem MxN (M e N informados pelo
usuário) e mostre sua matriz transposta em formato matricial.
"""

mat = []

userInputRangeM = int(input('informe o range M: '))
userInputRangeN = int(input('informe o range N: '))

for i in range(userInputRangeN):
    mat.append([])
    for j in range(userInputRangeM):
        userInputValue = int(input('Informe o valor: '))
        mat[-1].append(userInputValue)

for i in mat: print(i)

print()
print()
print()

reverseMat = []
for i in range(userInputRangeM):
    reverseMat.append([])
    for j in range(userInputRangeN):
        reverseMat[-1].append(mat[j][i])

for i in reverseMat: print(i)
