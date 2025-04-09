"""
Faça um programa em Python que solicite ao usuário informar uma sequência de
caracteres e exiba as diversas sequências de letras iguais.
"""

UserInput = input('informar uma sequência de caracteres: ')
LastChar = ''

for Char in UserInput:
    if Char == LastChar:
        print(Char, end='')
    else:
        print()
    LastChar = Char