"""
Ler um conjunto de valores correspondentes às notas que alunos obtiveram em
uma prova. Quando o valor fornecido for um número negativo, significa que não
existem mais notas para serem lidas.
○ Escrever o número de alunos
○ Escrever a maior nota
○ Escrever a menor nota
"""

points = 0
i = -1
big = 0
small = points + 1

while points >= 0:
    
    points = float(input('digite um número: '))
    if big < points:
        big = points
    elif small > points and points > 0:
        small = points

    i += 1
 

print(f'Teve {i} alunos, com a menor nota "{small}" e a maior nota "{big}"')