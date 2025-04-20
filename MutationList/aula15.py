"""
Faça um programa que permita que o usuário digite várias strings. A digitação
termina quando o usuário digitar “fim”. Armazene as strings em uma lista. Ao final,
exiba qual é a string maior e qual e a string menor (em quanƟdade de caracteres)
"""

userInputString = input('Digite algo: ')
listValuesString = []
minLenUserInputStringInt = len(userInputString)
maxLenUserInputStringInt = 0
while userInputString != 'fim':
    lenUserInputStringInt = len(userInputString)

    if minLenUserInputStringInt > lenUserInputStringInt:
        minLenUserInputStringInt = lenUserInputStringInt
    
    if maxLenUserInputStringInt < lenUserInputStringInt:
        maxLenUserInputStringInt = lenUserInputStringInt

    listValuesString.append(userInputString)
    userInputString = input('Digite algo: ')

print()
for i in listValuesString:
    lenItemValueInt = len(i)
    if lenItemValueInt == minLenUserInputStringInt:
        print(f'Menor string: {i}')    
    
    if lenItemValueInt == maxLenUserInputStringInt:
        print(f'Maior string: {i}')