# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.
ano = 0.0
pais_a = 80000
pais_b = 200000
taxa_crescimento_a = 0.030
taxa_crescimento_b = 0.015

while pais_a < pais_b:
    ano += 1
    pais_a = pais_a + (pais_a * taxa_crescimento_a)
    pais_b = pais_b + (pais_b * taxa_crescimento_b)

print(f"{ano:.0f} Anos.")