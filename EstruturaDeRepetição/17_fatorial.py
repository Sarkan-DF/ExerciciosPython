# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite o numero que deseja o fatorial: "))

if num == 0 or num == 1:
    print(f"Fatorial de {num} é: 1.")
else:
    num1 = num
    fatorial = num * (num - 1)
    num = num - 2

    for x in range(num):
        fatorial = fatorial * num
        num -= 1

    print(f"Fatorial de {num1} é: {fatorial}.")