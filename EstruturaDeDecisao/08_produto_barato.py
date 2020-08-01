# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

valor_produro1 = float(input("Qual preço do celular: "))
valor_produro2 = float(input("Qual preço do liquidificador: "))
valor_produro3 = float(input("Qual preço da TV: "))

menor_valor = valor_produro1
produto_menor_valor = "celular"
if valor_produro2 < menor_valor:
    menor_valor = valor_produro2
    produto_menor_valor = "liquidificador"
if valor_produro3 < menor_valor:
    menor_valor = valor_produro3
    produto_menor_valor = "TV"

print(f"O produto de menor valor é {produto_menor_valor} no valor de R${menor_valor:.2f}.")
