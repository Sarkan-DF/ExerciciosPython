# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango_peso = float(input("Quantos quilos de morango deseja comprar? "))
maca_peso = float(input("Quantos quilos de maça deseja comprar? "))

kg_morango_ate_cinco = 2.50
kg_morango_mais_cinco = 2.20
kg_maca_ate_cinco = 1.80
kg_maca_mais_cinco = 1.50

#calcula preço do morando
if morango_peso > 5.0:
    preco_morango = morango_peso * kg_morango_mais_cinco
else:
    preco_morango = morango_peso * kg_morango_ate_cinco

#calcula preço do maça
if maca_peso > 5.0:
    preco_maca = maca_peso * kg_maca_mais_cinco
else:
    preco_maca = maca_peso * kg_maca_ate_cinco

#calcula desconto de 10%
peso_total = morango_peso + maca_peso
preco_total = preco_morango + preco_maca

if peso_total > 8.0 or preco_total > 25.0:
    preco_total = preco_total - (preco_total * 0.10)

#print
print(f"Voçe comprou {morango_peso}Kg de morango e {maca_peso}Kg de maça no valor de R${preco_total}")