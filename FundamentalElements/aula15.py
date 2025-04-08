"""
Rosy é uma talentosa professora do Ensino Médio que já ganhou
muitos prêmios pela qualidade de sua aula. Seu reconhecimento foi
tamanho que foi convidada a dar aulas em uma escola da Inglaterra.
Tudo ocorreu bem para Rosy até o dia da prova. Acostumada a dar
notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova dos
alunos da Inglaterra. No entanto, os alunos acharam estranho, pois
na Inglaterra o sistema de notas é diferente: as notas devem ser
dadas como conceitos de A a E. O conceito A é o mais alto, enquanto
o conceito E é o mais baixo. Conversando com outros professores,
ela recebeu a sugestão de uƟlizar a tabela ao lado, relacionando as
notas numéricas com as notas de conceitos
● Escreva um programa que recebe uma nota no sistema numérico e
determina o conceito correspondente.
"""


Nota = int(input('Digite a nota: '))

if Nota >= 86:
    print('Nota A')
elif Nota >= 61:
    print('Nota B')
elif Nota >= 36:
    print('Nota C')
elif Nota >= 1:
    print('Nota D')
else:
    print('Nota E')