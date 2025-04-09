"""
Faça um programa que leia uma frase informada pelo usuário (incluindo espaços
em branco), conte a quantidade de espaços em branco e a quantidade de vezes
que aparecem as vogais a, e, i, o, u.
"""

String = 'Faça um programa que leia uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e a quantidade de vezes que aparecem as vogais a, e, i, o, u.'
Chars = ' abcd'

Count = 0

for i in String:
    if Chars.find(i.lower()) != -1:
        Count += 1

print(Count)