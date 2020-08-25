# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
# (resto da divisão).

numero = int(input("Digite o numero que deseja saber de é par ou impar: "))

if numero % 2 == 0:
     print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")
