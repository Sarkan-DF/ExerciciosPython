# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9)

farenheit = float(input("Digite a temperaruta em farenheit: "))
celsius = (5 * (farenheit-32) / 9)
print(celsius)
print(f"{farenheit}º farenheit são {celsius:.1f}º celsius.")