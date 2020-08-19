# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
# demais valores, sendo encerrado;
#A) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#B) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#C) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import sys
import math

numero_a = float(input("Digite o numero corespondente a 'A' na equação: "))
if numero_a == 0.0:
    print("Não é uma equação do segundo grau!")
    print("O programa sera encerado!")
    sys.exit()
numero_b = float(input("Digite o numero corespondente a 'B' na equação: "))
numero_c = float(input("Digite o numero corespondente a 'C' na equação: "))

delta = (numero_b ** 2) - (4 * numero_a * numero_c)

if delta < 0.0:
    print("A equação não possui raizes reais")
    print("O programa sera encerado!")
    sys.exit()
elif delta == 0.0:
    print("A equação possui apenas uma raiz real")
    raiz = (-numero_b + 0.0) / (2.0 * numero_a)
    print(f"A raiz é {raiz}")
else:
    print("A equação possui duas raiz reais!")
    delta = math.sqrt(delta)
    raiz1 = (-numero_b + delta) / (2 * numero_a)
    raiz2 = (-numero_b - delta) / (2 * numero_a)
    print(f"A raiz 1 é: {raiz1}")
    print(f"A raiz 2 é: {raiz2}")