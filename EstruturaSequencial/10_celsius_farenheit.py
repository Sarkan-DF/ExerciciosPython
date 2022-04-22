# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# F = (5 * (C+32) / 9).

ceusiu = float(input("Digite a temperatura em ceusius: "))
farenheit = (ceusiu * 9/5) + 32
print(f"{ceusiu:.1f}º ceusius são {farenheit:.1f}º farenheits.")