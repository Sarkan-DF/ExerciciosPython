# Faça um programa que leia 5 números e informe a soma e a média dos números.

nun1 = int(input("Didite o 1º numero: "))
nun2 = int(input("Didite o 2º numero: "))
nun3 = int(input("Didite o 3º numero: "))
nun4 = int(input("Didite o 4º numero: "))
nun5 = int(input("Didite o 5º numero: "))

lista_numeros = [nun1, nun2, nun3, nun4, nun5]
soma = 0

for x in lista_numeros:
    soma = soma + x

media = soma / 5

print(f"A soma dos numeros é: {soma}")
print(f"A media dos numeros é: {media}")
