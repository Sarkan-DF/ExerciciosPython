# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
# ele mostre os números um ao lado do outro.

for x in range(1,21):
    print(x)

for x in range(1,21):
    print(f"{x} ", end="")