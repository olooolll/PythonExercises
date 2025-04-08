"""
Faça um programa que leia um conjunto de valores positivos maiores que zero.
Quando for fornecido um número negativo, deve-se terminar a leitura. Ao fim,
seu programa deve imprimir o maior valor lido
"""

n = 0
big = 0

while n >= 0:
    if big < n:
        big = n
    else:
        n = float(input('Digite um número: '))

print(f'O maior número foi "{big}"')