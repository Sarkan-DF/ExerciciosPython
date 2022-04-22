# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

pais_a = float(input("Digite a população do pais 'A': "))
pais_b = float(input("Digite a população do pais 'B': "))
taxa_crescimento_a = float(input("Digite a taxa de crescimento do pais 'A': "))
taxa_crescimento_b = float(input("Digite a taxa de crescimento do pais 'B': "))
taxa_crescimento_a = taxa_crescimento_a / 100
taxa_crescimento_b = taxa_crescimento_b / 100

ano = 0.0

while pais_a < pais_b:
    ano += 1
    pais_a = pais_a + (pais_a * taxa_crescimento_a)
    pais_b = pais_b + (pais_b * taxa_crescimento_b)

print(f"{ano:.0f} Anos.")