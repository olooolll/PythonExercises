"""
Faça uma função que recebe um número inteiro e retorna: 1 se o número é
positivo, -1 se o número é negativo ou 0 se o número for igual a zero.
"""
def NumberCompreEntion(n):
    if n > 0:
        return 1
    if n == 0:
        return 0
    return -1


######### Programa Principal ############## 


userInputNumber = int(input('Informe um número: '))
result = NumberCompreEntion(userInputNumber)

if result > 0:
    print('O número é positivo: ', result)
elif result == 0:
    print('O número é zero: ', result)
else:
    print('O número é Negativo: ', result)