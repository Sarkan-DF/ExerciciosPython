# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles.

num1 = int(input("Digite o valor inicial: "))
num2 = int(input("Digite o valor final: "))
while num1 > num2:
    print("Valor final deve ser maior que inicial.")
    num1 = int(input("Digite o valor inicial: "))
    num2 = int(input("Digite o valor final: "))


for x in range(num1+1, num2):
    print(f'{x} ', end='')