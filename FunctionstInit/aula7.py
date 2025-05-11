"""
Faça uma função que recebe um número inteiro e retorna a quantidade de dígitos
desse numero: -12478 > 5 
"""

def LenInt(int):
    if int < 0:
        int = -int

    count = 0
    while int > 0:
        int //= 10

        count +=1

    return count


########## Proeto Principal #########


userInputValue = int(input('Informe um número inteiro: '))

print(f'O número "{userInputValue}" tem {LenInt(userInputValue)} caracters')