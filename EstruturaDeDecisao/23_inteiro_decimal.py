# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função
# de arredondamento.

numero_float = float(input("Digite o numero que deseja saber se é inteiro ou decinal: "))

numero_decimal = round(numero_float)

if numero_float == numero_decimal:
    print("È inteiro!")
else:
    print("È decimal!")
