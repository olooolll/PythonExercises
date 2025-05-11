"""
Faca uma função que recebe uma palavra e retorna o numero de letras que a
palavra possui
"""

def lenString(string):
    count = 0
    for i in string:
        count += 1
    
    return count

########### Programa Principal ###########

userInputString = input('Informe uma string: ')

print(f'A sting "{userInputString}" tem {lenString(userInputString)} caracter')