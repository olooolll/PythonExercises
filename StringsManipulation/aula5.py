"""
Faça um programa que leia uma frase e retire a primeira ocorrência de uma letra da frase
● Entradas: frase e letra a ser removida (1ª ocorrência da esquerda para a direita)
"""

String = '(1ª ocorrência da esquerda para a direita)'
Char = 'a'
NewString = ''
Count = 0

for i in String:
    
    if Char == i and Count < 1:
        Count = 1
    else:
        NewString += i

print(String)
print(NewString)