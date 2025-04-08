"""
Faça um algoritmo que leia um número inteiro X. A partir dele tem-se um novo
X de acordo com a seguinte regra
○ se X é par, X = X / 2
○ se X é impar, X = 3 * X + 1
● O algoritmo deve escrever todos os valores até parar. A condição de parada é
quando X tiver o valor final de 1. Exemplo:
"""


x = int(input('Figite um numero: '))

while x != 1:
    if x % 2 == 0:
        x = x / 2
    else:
        x = x * 3 + 1

    print(int(x), end=' | ')