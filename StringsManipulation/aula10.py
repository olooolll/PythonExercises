"""
Faça um programa que leia um nome e mostre-o na tela na vertical e em formato
de escada. Ex.:
"""

String = 'FULANO'
StringLen = 1

for i in String:
    for j in range(0,StringLen):
        print(String[j] ,end='')
        
    StringLen += 1
    print()