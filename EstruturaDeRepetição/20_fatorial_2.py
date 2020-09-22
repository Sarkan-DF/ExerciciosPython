# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.

num = int(input("Digite o numero que deseja o fatorial: "))

while num < 0 or num > 16:
    print("Só são permitidos numeros positivos e menores que 17!")
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

var = input(("Deseja calcular mais um fatorial? 'S' para sim ou 'N' para não: "))
var = var.upper()

while var == "S":
    num = int(input("Digite o numero que deseja o fatorial: "))

    while num < 0 or num > 16:
        print("Só são permitidos numeros positivos e menores que 17!")
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

    var = input(("Deseja calcular mais um fatorial? 'S' para sim ou 'N' para não: "))
    var = var.upper()