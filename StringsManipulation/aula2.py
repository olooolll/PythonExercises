"""
Faça um programa que leia uma frase e imprima a quantidade de caracteres que
essa string contém, com exceção de espaços em branco.
"""

String = 'imprima a quantidade'

Count = 0

for i in String:
    if i != ' ':
        Count += 1

# or

StringReplace = String.replace(' ', '')
Count = len(StringReplace)

print(Count)