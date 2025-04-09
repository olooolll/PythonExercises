"""
Faça um programa que leia uma string e imprima “Sim” se é palíndromo e “Nao”,
caso contrário.
○ Palíndromo: diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a
direita ou vice-versa. Por exemplo: “arara” é um palíndromo
● Considere como entrada apenas palavras com letras minúsculas e sem espaços

"""

String = 'arara'
ReverseString =  String[::-1]

if String == ReverseString:
    print('Sim')
else:
    print('Nao')