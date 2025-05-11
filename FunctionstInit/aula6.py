"""
Faca uma função que recebe uma frase e retorna o numero de palavras que a
frase contem.
"""

def CountWords(string):
    listChars = [' ', ',', '.', ';', ':', '!', '!']

    count = 1
    for i in (range((len(string) - 1))):
        if string[i + 1] in listChars:
            count += 1
    
    if string[-1] in listChars:
        count -= 1

    return count


########### Programa Principal ###########


userInputString = input('Informe um frase: ')

print(f'A sua frase "{userInputString}" tem {CountWords(userInputString)} pala')