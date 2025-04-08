"""
Faça um programa que leia um número X e apresente os resultados da sua
tabuada.
● Por exemplo: Com X igual a 3, o algoritmo deve escrever:
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
4 x 3 = 12
5 x 3 = 15
6 x 3 = 18
7 x 3 = 21
8 x 3 = 24
9 x 3 = 27

"""

x = float(input('Insira um número: '))

for i in range(1, 11):
    print(f'{i} x {x} = {i * x:.2f}')