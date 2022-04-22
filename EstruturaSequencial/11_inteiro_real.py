# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo.
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.

inteiro1 = int(input("Digite o 1º inteiro: "))
inteiro2 = int(input("Digite o 2º inteiro: "))
real = float(input("Digite o numero real: "))

a = (inteiro1 * 2) * (inteiro2 / 2)
b = (inteiro1 * 3) + real
c = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {a}")
print(f"A soma do triplo do primeiro com o terceiro é: {b}")
print(f"O terceiro elevado ao cubo é: {c}")