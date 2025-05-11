"""
Faça uma função que recebe duas strings. Admita que elas terão o mesmo
número de caracteres. A função deve retornar uma string com as letras
intercaladas: Instituto, FederalSP = IFnesdteirtaultSoP
"""

def MescleStrings(string1, string2):
    newString = ''

    for i in range(len(string1)):
        newString += (string1[i] + string2[i])

    return newString


########### Programa Principal ###########

userInputString1 = input('Informe uma palavra: ')
userInputString2 = input('Informe outra palavra: ')

print(f'A junção das duas palavras é "{MescleStrings(userInputString1, userInputString2)}"')