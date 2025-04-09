"""
Faça um programa que leia uma a entrada de um número inteiro positivo ou
negativo e mostre a quantidade de dígitos desse número.
"""

String = '-16546'
Count = 0

for i in String:
    if i.isdigit():
        Count += 1

print(Count)