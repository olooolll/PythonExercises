"""
Faça um programa que leia 10 valores e armazene em uma lista. Após isso, faça:
○ Imprima todos os valores lidos
○ Imprima a soma de todos eles
○ Imprima apenas os números pares
"""
listInt = []

i = 1
while i <= 10:
    userInputInt = int(input('Digite um valor: '))
    listInt.append(userInputInt)
    i += 1

print()
print('Todos os valores lidos: ', end='')
for i in listInt:
    print(i, end=', ')

print()
sumTotal = 0
for i in listInt:
    sumTotal += i
print(f'A soma de todos eles: {sumTotal}')

print('Apenas os números pares: ', end='')
for i in listInt:
    if i % 2 == 0:
        print(i, end=', ')
