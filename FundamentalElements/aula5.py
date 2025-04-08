"""
Faça um algoritmo que leia 3 notas de um aluno, onde a primeira nota possui
peso um, a segunda possui peso dois e a terceira peso três. Calcule a média
ponderada do aluno baseada nos pesos e escreva na tela.
○ Média ponderada = (peso1 * nota1 + peso2 * nota2 + peso3 * nota3)
 (peso1 + peso2 + peso3)
"""

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

print(f'A média das notas do aluno é {(1 * nota1 + 2 * nota2 + 3 * nota3) / (1 + 2 + 3)}')