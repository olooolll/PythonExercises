"""
Dado duas strings A e B, faça um programa que imprima “Sim” se A e B são
anagramas e “Nao”, caso contrário.
○ Anagrama: transposição de letras de palavra ou frase para formar outra palavra ou frase
diferente. Por exemplo: “roma” e “amor” são anagrama
Considere como entrada apenas palavras com letras minúsculas
"""

StringA = 'roma'
StringB = 'amor'
Bool = 'Nao'


if len(StringA) == len(StringB):
    for Char in StringA:
        if StringB.find(Char) != -1:
            Bool = 'Sim'
            
        else:
            Bool = 'Nao'
        break

print(Bool)