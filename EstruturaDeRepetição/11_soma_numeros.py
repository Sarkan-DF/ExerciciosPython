# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite o valor inicial: "))
num2 = int(input("Digite o valor final: "))
while num1 > num2:
    print("Valor final deve ser maior que inicial.")
    num1 = int(input("Digite o valor inicial: "))
    num2 = int(input("Digite o valor final: "))

soma = 0

for x in range(num1+1, num2):
    print(f'{x} ', end='')
    soma = x + soma

print(f"\nA soma de todos os numeros acima é {soma}.")