"""
Faça um programa que construa duas listas A e B de 5 elementos cada. Após isso
leia 10 valores e adicione os 5 primeiros na lista A e os 5 úlƟmos na lista B. Crie
uma terceira lista C, composta pela soma dos elementos de A e B que se
encontram em posições correspondentes. Após isso, escreva o conteúdo das listas
A, B e C, com elementos separados por vírgula

"""
aList = []
bList = []
sumList = []

i = 0
while i < 10:
    inputUserInt = int(input('Digite um valor: '))

    if i < 5:
        aList.append(inputUserInt)
    else:
        bList.append(inputUserInt)

    i += 1

i = 0
while i < 5:
    sumList.append(aList[i] + bList[i])

    i += 1

print('Lista A: ', end='')
for i in aList:
    print(f'{i}', end=', ')

print()
print('Lista B: ', end='')
for i in bList:
    print(f'{i}', end=', ')

print()
print('Lista C: ', end='')
for i in sumList:
    print(f'{i}', end=', ')

# 3 -5 23 -156 9
# -345 8 76 44 -6