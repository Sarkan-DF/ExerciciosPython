# Faça um programa que calcule o mostre a média aritmética de N notas.

quanti_notas = int(input("Quantas notas dedeja fazer a media? "))
media = 0.0
soma_nota = 0.0
nota = 0.0

for i in range(quanti_notas):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    soma_nota = soma_nota + nota

media = soma_nota / quanti_notas

print(f"A media das {quanti_notas} notas é de: {media:.2f}")
