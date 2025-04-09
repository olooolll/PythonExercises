"""
Faça um programa que leia uma String e escreva:
○ O número de caracteres que a string contém
○ Caractere por caractere, utilizando laço de repetição
○ Caractere por caractere, porém na ordem inversa, utilizando laço de repetição
"""

String = 'caracteres'
LenString = len(String)

print(LenString)

for i in String:
    print(i, end=' ')

print()
LenString -= 1

for i in String:
    print(String[LenString], end=' ')
    LenString -= 1