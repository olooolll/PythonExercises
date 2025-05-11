"""
Faça uma função que recebe como parâmetros a base e o expoente e retorna o
valor da potência. Não é permitido utilizar nenhuma função do Python para o
calculo da potência e nem o uso do operador **
"""

def Potency(base, exponent):
    result = base
    i = 1
    while i < exponent:
        result *= base

        i += 1

    return result


########## Programa Principal ##########


userInputBase = int(input('Informe o valor da base: '))
userInputExponent = int(input('Informe o valor da expoente: '))

print(f'O resultado de {userInputBase} ** {userInputExponent} = {Potency(userInputBase, userInputExponent)}')