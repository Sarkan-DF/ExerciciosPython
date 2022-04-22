# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o 1º numero: "))
num2 = int(input("Digite o 2º numero: "))
num3 = int(input("Digite o 3º numero: "))

if (num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux
if (num2 > num1):
    aux = num2
    num2 = num1
    num1 = aux
if (num3 > num2):
    aux = num3
    num3 = num2
    num2 = aux

print(f"numero em ordem decrecente: {num1},{num2},{num3}")
