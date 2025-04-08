"""
Faça um programa que leia A, B e C de uma equação do segundo grau, conforme
abaixo:
○ Ax² + Bx + C
● Calcule as raízes da equação. O algoritmo deve informar caso a equação não
tenha raízes reais (Delta menor que zero)
"""

a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

Delta = b ** 2 - 4 * a * c

print(Delta)
if not Delta < 0:
    x1 = (-b + Delta ** 0.5) / (2 * a)
    x2 = (-b - Delta ** 0.5) / (2 * a)

    print(x1, x2)
else:
    print('A equação não tem raízes reais (Delta menor que zero)')