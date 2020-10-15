# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# é divisível somente por ele mesmo e por 1.

num = int(input("Digite o numero que deseja verificar se é primo: "))
contador = 0

for x in range(2,num):
    print(x)
    if num % x == 0:
        contador += 1

if contador == 0:
    print("É primo!")
else:
    print("Não é primo!")