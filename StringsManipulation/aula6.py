"""
Faça um programa que leia uma frase e retire a última ocorrência de uma letra
da frase
● Entradas: frase e letra a ser removida (última ocorrência da esquerda para a direita)
"""

String = '(última ocorrência da esquerda para a direita)'
Char = 'q'
NewString = ''
StringRevers = String[::-1]
Count = 0

for i in StringRevers:
    
    if Char == i and Count < 1:
        Count = 1
    else:
        NewString += i

print(String)
print(NewString[::-1])