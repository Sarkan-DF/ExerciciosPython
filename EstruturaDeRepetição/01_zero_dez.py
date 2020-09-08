# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

numero = int(input("Digite um numero de 0 a 10: "))

while numero < 0 or numero > 10:
    print("Numero incorreto!")
    numero = int(input("Favor digitar um numero de 0 a 10: "))

print("Numero correto parabens!")