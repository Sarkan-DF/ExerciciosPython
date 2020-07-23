# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
# é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
# a serem compradas e o preço total.

import math

area_ha_ser_pintada = float(input("Favor informar a area a ser pintada em M²: "))

lata_pinta_metros = 18 * 3
litros_lata = 18
preco_lata = 80.0

quantidade_latas = math.ceil(area_ha_ser_pintada / lata_pinta_metros)
total_gastos = quantidade_latas * preco_lata

print(f"Será nescessarias {quantidade_latas:.0f} lata(s) de tinta.")
print(f"E você gastará R${total_gastos:.2f}.")
