"""
Faça um programa que leia três números e informe o maior entre eles
"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n3:
    print(f'O maior número é {n2}')
elif n1 == n2 and n2 == n3:
    print(f'Todos os números são iguais')
else:
    print(f'O maior número é {n3}')
