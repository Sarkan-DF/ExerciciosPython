# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.

print("Favor digitar abaixo 10 numeros:" )

lista_numeros = []
n = 1
while n < 11:
    lista_numeros.append(int(input(f"{n}º numero: ")))
    n += 1

par = 0
impar = 0

for x in lista_numeros:
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Nesta sequencia são {par} numeros pares e {impar} numeros impares.")