"""
Faça um programa que leia o número de linhas M de uma matriz e o número N de
colunas. Após isso, leia MxN valores e coloque-os na matriz. Por fim, imprima a
matriz em formato matricial
"""

mat = []
userInputRowValue = int(input('Informe o valor das linhas: '))
userInputColValue = int(input('Informe o valor das colunas: '))

i = 0
while i < userInputRowValue:
    mat.append([])

    j = 0
    while j < userInputColValue:
        userInputValues = int(input('Informe os valores: '))
        mat[-1].append(userInputValues)
        
        j += 1
    i += 1

for row in mat:
    print(row)