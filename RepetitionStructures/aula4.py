"""
Fazer um programa que apresenta o total da soma dos números pares até 100 (2 + 4 + 6 + ... + 98 + 100)
"""
sum = 0
for i in range(2,101,2):
    sum += i
    if i != 100:
        print(f'{i}', end=' + ')
    else:
        print(f'{i} = {sum}')

