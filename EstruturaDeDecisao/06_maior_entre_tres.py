# Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))
numero3 = float(input("Digite o 3º numero: "))

maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

print(maior)