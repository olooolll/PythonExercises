
"""
Faça um algoritmo que leia um número inteiro N e calcule o seu fatorial.
Lembrando:
○ Fatorial de 5 = 5! = 5 * 4 * 3 * 2 * 1 = 120
○ Fatorial de N = N! = N * (N – 1) * ... * 2 * 1
○ Fatorial de 0 = 0! = 1
"""

n = int(input('Digite um número: '))

i = n
sum = n
if not n:
    print('0 = 0! = 1')

while i > 1:
    i -= 1
    sum *= i
    print(f'{n}! {i} = {sum}')