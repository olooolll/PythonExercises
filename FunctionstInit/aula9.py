"""
Escreva uma função que recebe um número inteiro positivo entre 0 e 99 e
retorne a string contendo o número por extenso
"""

def ExtencionNumbers(int):
    string = ''
    primaris = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez']
    decimals = ['Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove']
    othersDecimals = ['Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sesenta', 'Setenta', 'Oitenta', 'Noventa']
    
    if int <= 10:
        string += primaris[int]
    elif int <= 19:
        int -= 10
        string += decimals[int - 1]
    else:
        string += othersDecimals[(int // 10) - 2]
        if int % 10:
            string += ' e '
            string += primaris[(int % 10)]


    return string

########## Programa Principal ##########

userInputValue = int(input('Informe um número: '))

print(f'O número por extenso "{ExtencionNumbers(userInputValue)}"')