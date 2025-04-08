"""
Faça um programa que leia 3 valores inteiros (A, B e C), coloque-os em ordem
crescente (ou seja, ao final A deve armazenar o menor valor, C o maior e B o
valor do meio)
"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 > n3:
    print(f'{n3}, {n2}, {n1}')
elif n1 > n3 > n2:
    print(f'{n2}, {n3}, {n1}')
elif n2 > n1 > n3:
    print(f'{n3}, {n1}, {n2}')
elif n2 > n3 > n1:
    print(f'{n1}, {n3}, {n2}')
elif n3 > n1 > n2:
    print(f'{n2}, {n1}, {n3}')
else:
    print(f'{n1}, {n2}, {n3}')