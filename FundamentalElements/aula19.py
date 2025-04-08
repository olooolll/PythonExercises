"""
Uma determinada loja está fazendo promoções de vendas. Qualquer compra que
um cliente fizer até R$ 100,00 receberá 5% de desconto. Se a compra for maior
que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior
ou igual a R$ 200,00, o desconto será de 20%.
● Faça um programa que calcule o desconto do total da compra de um cliente, e
informe também, o total a pagar já com os descontos
"""

ValorDaCompra = float(input('Digite o valor da compra: '))

if ValorDaCompra >= 200:
    print(f'O valor da compra é {ValorDaCompra * 0.8:.2f}')
elif ValorDaCompra > 100:
    print(f'O valor da compra é {ValorDaCompra * 0.9:.2f}')
else:
    print(f'O valor da compra é {ValorDaCompra * 0.95:.2f}')