"""
Fazer um programa que apresenta o total da soma dos números de 0 até 100 (0 + 1 + 2 + ... + 99 + 100)
"""
sum = 0
for i in range(0, 101):
    if i != 100 :
        print(f'{i} + ', end='')
    else:
        print(f'{i}', end=' = ')
    
    sum += i - 1

print(sum)