# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

print("Digite a seguir base e expoente para fazer a potenciação.\n")
base = int(input("Digite o numero da base: "))
expoente = int(input("Digite o numero do expoente: "))

potenciacao = 1

for x in range(1, expoente+1):
    potenciacao *= base

print(f"{base} elevado a {expoente} é = {potenciacao}")