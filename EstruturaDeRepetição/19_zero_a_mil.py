# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
import sys

quant_numeros = int(input("Com quantos numeros deseja seu comjunto? "))

conjunto = []
n = 1
while n < quant_numeros+1:
    conjunto.append(int(input(f"Digite seu {n} numero: ")))
    n += 1

for x in conjunto:
    if x < 0 or x > 1000:
        print("Só são validoes numeros de 0 a 1000!")
        sys.exit()

maior = max(conjunto)
menor = min(conjunto)
soma = 0

for x in conjunto:
    soma = soma + x

print(f"Maior {maior}, menor {menor} e soma {soma}")