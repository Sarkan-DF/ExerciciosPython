# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# # é divisível somente por ele mesmo e por 1.
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
# divisível.

num = int(input("Digite o numero que deseja verificar se é primo: "))
contador = 0
lista_divisivel = []

for x in range(2,num):
    if num % x == 0:
        lista_divisivel.append(x)
        contador += 1

lista_divisivel = str(lista_divisivel).strip('[]')

if contador == 0:
    print(f"{num} É primo!")
else:
    print(f"{num} Não é primo! É divisivel por {lista_divisivel}, 1 e {num}")