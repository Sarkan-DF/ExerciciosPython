# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
# na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input("Qual valor deseja sacar lembrando que o valor minimo é R$10,00 e o maximo R$600,00: "))
nota_um = nota_cinco = nota_dez = nota_cinquenta = nota_cem = 0

while(valor_saque < 10.0 or valor_saque >600.00):
  print("Valor incoreto!")
  valor_saque = int(input("Qual valor deseja sacar lembrando que o valor minimo é R$10,00 e o maximo R$600,00: "))

#descobrindo nota 100
nota_cem, valor_saque = divmod(valor_saque,100)

#descobrindo nota 50
nota_cinquenta, valor_saque = divmod(valor_saque,50)

#descobrindo nota 10
nota_dez, valor_saque = divmod(valor_saque,10)

#descobrindo nota 5
nota_cinco, nota_um = divmod(valor_saque,5)

print(f"Para o saque no valor de R${valor_original} sairá do caixa::")

if nota_cem > 0:
  print(f"{nota_cem} nota(s) de cem.")
if nota_cinquenta > 0:
  print(f"{nota_cinquenta} nota(s) de cinquenta.")
if nota_dez > 0:
  print(f"{nota_dez} nota(s) de dez.")
if nota_cinco > 0:
  print(f"{nota_cinco} nota(s) de cinco.")
if nota_um > 0:
  print(f"{nota_um} nota(s) de um.")
