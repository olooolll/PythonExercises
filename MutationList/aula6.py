"""
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros.
Em seguida leia um número inteiro X. Ao fim escreva se o elemento está na lista ou
não.
○ A respeito de funções de lista, só é permiƟdo o uso da função append() e len()
"""
userInputNInt = int(input('Digite um valor inteiro: '))
listValuesInt = []

i = 0
while i < userInputNInt:
    userInputValueInt =int(input('Digite um valor inteiro para adicionar a lista: '))
    listValuesInt.append(userInputValueInt)
    i += 1

userInputXInt = int(input('Informe um número para verificar se está na lista: '))

findNumberBoll = False
for i in listValuesInt:
    if i == userInputXInt:
        findNumberBoll = True

if findNumberBoll:
    print('O número está na lista')
else:
    print('O número não está na lista')