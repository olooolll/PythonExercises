"""
Faça um programa que permita que o usuário digite várias strings. A digitação
termina quando o usuário digitar “fim”. Leia um caractere X e remova a primeira
ocorrência desse caractere em todas as strings da lista que possuírem tal caractere.
Caso uma string se transforme em string vazia, ela deve ser removida da lista.
Mostre a lista final.
"""

userInputString = input('Digite algo: ')
valuesUserInputList = []

while userInputString != 'fim':
    valuesUserInputList.append(userInputString)
    userInputString = input('Digite algo: ')


userInputXChar = input('Digite o caracter: ')
i = 0
while i < len(valuesUserInputList): 
    
    newString = ''
    findChar = False
    for char in valuesUserInputList[i]:
        if char == userInputXChar and not findChar:
            findChar = True
        else:
            newString += char

    valuesUserInputList[i] = newString

    i += 1

i = 0
while i < len(valuesUserInputList):
    if valuesUserInputList[i] == '':
        del valuesUserInputList[i]
        i -= 1

    i += 1

print(valuesUserInputList)