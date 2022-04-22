# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

tipo_de_carne = input("Qual tipo de carne deseja comprar? 'F' para File Duplo, 'A' para Alcatra e 'P' para 'Picanha': ")
tipo_de_carne = tipo_de_carne.upper()
kilo_carne = float(input("Quantos kilos de carne deseja comprar? "))
forma_pagamento = input("Forma de pagamento? 'T' para cartão tabajara e 'O' para outras formas de pagamento: ")
forma_pagamento = forma_pagamento.upper()
valor_kilo_file_menos = 4.90
valor_kilo_file_mais = 5.80
valor_kilo_alcatra_menos = 5.90
valor_kilo_alcatra_mais = 6.80
valor_kilo_picanha_menos = 6.90
valor_kilo_picanha_mais = 7.90
desconto = 0.0
preco_total = 0.0

#Preço total file
if tipo_de_carne == "F":
    if kilo_carne <= 5.0:
        preco_total = kilo_carne * valor_kilo_file_menos
    else:
        preco_total = kilo_carne * valor_kilo_file_mais

#Preço total alcatra
if tipo_de_carne == "A":
    if kilo_carne <= 5.0:
        preco_total = kilo_carne * valor_kilo_alcatra_menos
    else:
        preco_total = kilo_carne * valor_kilo_alcatra_mais

#Preço total picanha
if tipo_de_carne == "P":
    if kilo_carne <= 5.0:
        preco_total = kilo_carne * valor_kilo_picanha_menos
    else:
        preco_total = kilo_carne * valor_kilo_picanha_mais

preco_total_sem_desconto = preco_total

#desconto cartão
if forma_pagamento == "T":
    desconto = preco_total * 0.05
    preco_total = preco_total - desconto

#Tipo carne
if tipo_de_carne == "F":
    tipo_de_carne = "File Duplo"
elif tipo_de_carne == "A":
    tipo_de_carne = "Alcatra"
elif tipo_de_carne == "P":
    tipo_de_carne = "Picanha"

#forma de pagamento
if forma_pagamento == "T":
    forma_pagamento = "Cartão Tabajara"
elif forma_pagamento == "O":
    forma_pagamento = "Outros"

print(f"Tipo carne: {tipo_de_carne}")
print(f"Peso: {kilo_carne} Kilo(s)")
print(f"Preço total: R${preco_total_sem_desconto:.2f}")
print(f"Tipo de pamento: {forma_pagamento}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${preco_total:.2f}")
