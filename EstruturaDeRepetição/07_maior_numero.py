# Faça um programa que leia 5 números e informe o maior número.

nun1 = int(input("Didite o 1º numero: "))
nun2 = int(input("Didite o 2º numero: "))
nun3 = int(input("Didite o 3º numero: "))
nun4 = int(input("Didite o 4º numero: "))
nun5 = int(input("Didite o 5º numero: "))

lista_numeros = [nun1, nun2, nun3, nun4, nun5]

maior = max(lista_numeros)

print(maior)