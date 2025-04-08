"""
Uma livraria está fazendo uma promoção para pagamento à vista. O comprador
pode escolher entre dois critérios para pagamento:
○ Critério A: R$ 0,25 por livro + R$ 7,50 fixo
○ Critério B: R$ 0,50 por livro + R$ 2,50 fixo
● Faça um programa que o usuário informa a quanƟdade de livros e o algoritmo
informa os valores para cada um dos critérios e indica qual o critério de
pagamento é mais vantajoso para o cliente
"""

QuantidadeDeLivros = int(input('Digite a quantidade de livros: '))

a = (0.25 * QuantidadeDeLivros) + 7.5
b = (0.5 * QuantidadeDeLivros) + 2.5

if a > b:
    print(f'valor dos Critérios A = {a} e B = {b}, sendo mais vantajoso o B')
else:
    print(f'valor dos Critérios A = {a} e B = {b}, sendo mais vantajoso o A')
    