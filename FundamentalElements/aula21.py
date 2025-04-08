"""
Faça um programa que leia dois números inteiros X e Y e imprima todos os
números de X até Y.
○ Assuma que X sempre será menor que Y;
○ Altere o programa para que seja permitida a entrada dos números em qualquer ordem e mostre
a sequência em ordem crescente.
"""

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: ')) + 1

for i in range(x, y):
    print(i)