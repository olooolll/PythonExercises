"""
Ler um conjunto de valores correspondentes às notas que alunos obtiveram em
uma prova. Quando o valor fornecido for um número negativo, significa que não
existem mais pontos para serem lidos
○ Escrever quantas notas são maiores ou iguais a 6.0
○ Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
○ Escrever quantos notas são menores que 4.0
"""

n = 0

flag = True
n1 = 0
n2 = 0 
n3 = 0
while flag:
    n = float(input('Digite o valor da nota: '))

    if n >= 6:
        n1 += 1

    elif n >= 4:
        n2 += 1

    elif n >= 0:
        n3 += 1

    else:
        flag = False

print(f'{n1} notas são maiores ou iguais a 6.0')
print(f'{n2} notas são maiores ou iguais a 4.0 e menores que 6.0')
print(f'{n3} notas são menores que 4.0')