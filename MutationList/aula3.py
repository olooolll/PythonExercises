"""
Faça um programa que leia dados de temperatura durante uma semana (7 leituras),
armazenando em uma lista. Após ter criado a lista, escreva quantos dias dessa semana a
temperatura esteve acima da média.
"""
listOfTemp = []
dayOfWeek = 7
sumTemp = 0
daysOfWeekMostAvaregeTemp = 0

i = 0
while i < dayOfWeek:
    userInputTempFloat = float(input('Digite o calor da temperatura: '))
    listOfTemp.append(userInputTempFloat)
    sumTemp += userInputTempFloat

    i += 1

avaregeTemp = sumTemp / dayOfWeek

for i in listOfTemp:
    if i > avaregeTemp:
        daysOfWeekMostAvaregeTemp += 1

print(f'{daysOfWeekMostAvaregeTemp} dias dessa semana a temperatura esteve acima da média {avaregeTemp}')