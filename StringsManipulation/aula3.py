"""
Faça um programa que leia uma frase e imprima o número de palavras que a
frase contém.
"""

String = 'Faça um programa que leia uma frase e imprima o número de palavras que a frase contém.'
Chars = 'abcçdefghijklmnopqrstuvwxyz0123456789éú'

Count = 0

for i in String:
    if Chars.find(i.lower()) == -1:
        Count += 1


print(Count)