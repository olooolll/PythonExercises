"""
Crie uma função para exibir os algarismos de um número inteiro positivo
de forma invertida. Não é permitida a conversão para string. Exemplo:
326
6
2
3
"""

def printrl(int):
    if int == 0:
        return 0

    print(int % 10)
    
    printrl(int // 10)

print(printrl(624))