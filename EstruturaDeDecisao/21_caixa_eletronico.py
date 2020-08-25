# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
# na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

import math

valor = int(input("Digite o valor a ser sacado entre R$10 e R$600,00: "))
valor_original = valor

if (valor < 10) or (valor > 600):
    print("Valor Invalido de saque!")

else:
    nota_cem = valor/100
    nota_cem = math.floor(nota_cem)
    valor = valor - (nota_cem * 100)

    nota_cinquenta = valor/50
    nota_cinquenta = math.floor(nota_cinquenta)
    valor = valor - (nota_cinquenta * 50)

    nota_dez = valor/10
    nota_dez = math.floor(nota_dez)
    valor = valor - (nota_dez * 10)

    nota_cinco = valor/5
    nota_cinco = math.floor(nota_cinco)
    valor = valor - (nota_cinco * 5)

    nota_um = valor/1
    nota_um = math.floor(nota_um)
    valor = valor - (nota_um * 1)

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