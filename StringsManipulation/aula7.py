"""
Faça um programa que leia uma frase e retire todas as ocorrência de uma letra
da frase
● Entradas: frase e letra a ser removida
"""

String = 'Faça um programa que leia uma frase e retire todas as ocorrência de uma letra da frase'
Char = 'a'
NewString = ''

for i in String:
    if i  != Char:
        NewString += i
    
print(String)
print(NewString)