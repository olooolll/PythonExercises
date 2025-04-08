"""
Faça um programa que leia 2 valores inteiros (A e B), mostre-os na tela em ordem
crescente (ou seja, ao final A deve armazenar o menor valor e B o maior valor)
"""


a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))


if a > b:
    print(f'{b}, {a}')
else:
    print(f'{a}, {b}')
