"""
Faça uma função que recebe a data de nascimento (“dd/mm/aaaa”) e
retorna a string contendo a data com o mês por extenso. Data de
Nascimento: 29/10/1973  29 de Outubro de 1973.
"""

def SelectMonth(string):
    listsStrings = []
    chars = ''

    for i in string:
        if i == '/':
            listsStrings.append(chars)
            chars = ''
        else:
            chars += i
    listsStrings.append(chars)

    if listsStrings[1] == '01':
        listsStrings[1] = 'Janeiro'
            
    if listsStrings[1] == '02':
        listsStrings[1] = 'Fevereiro'
            
    if listsStrings[1] == '03':
        listsStrings[1] = 'Março'
            
    if listsStrings[1] == '04':
        listsStrings[1] = 'Abril'
            
    if listsStrings[1] == '05':
        listsStrings[1] = 'Maio'
            
    if listsStrings[1] == '06':
        listsStrings[1] = 'Junho'
            
    if listsStrings[1] == '07':
        listsStrings[1] = 'Julho'
        
    if listsStrings[1] == '08':
        listsStrings[1] = 'Agosto'
        
    if listsStrings[1] == '09':
        listsStrings[1] = 'Setembro'
        
    if listsStrings[1] == '10':
        listsStrings[1] = 'Outubro'
    
    if listsStrings[1] == '11':
        listsStrings[1] = 'Novembro'
        
    if listsStrings[1] == '12':
        listsStrings[1] = 'Dezembro'
        

    return listsStrings



########### Programa Principal ###########


userInputDate = input('Informe o dia ano e mês: ')
result = SelectMonth(userInputDate)

print(f'{result[0]} de {result[1]} de {result[2]}')