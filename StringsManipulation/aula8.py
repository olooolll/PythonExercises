"""
Faça um programa que leia uma frase e mostre a quantidade total de uma letra
informada pelo usuário presente na frase.
● Entradas: frase e letra a ser contada
"""

String = 'Faça um programa que leia uma frase e retire todas as ocorrência de uma letra da frase'
Char = 'a'
Count = 0

for i in String:
    if i  == Char:
        Count += 1
    
print(String)
print(Count)