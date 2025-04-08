"""
● Faça um programa que leia dois inteiros x e y, e calcule e imprima o valor de z:
○ z = (x² + y²)
 (x - y)²
"""

x = int(input('Digite o numero de X: '))
y = int(input('Digite o numero de Y: '))

z = (x ** 2 + y ** 2) / (x - y) ** 2

print(f'O valor de Z = {z}')