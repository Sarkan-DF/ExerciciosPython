"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
"""


def numeros_primos():
    num = int(input("Favor digitar o numero que deseja saber se é primo: "))
    contador = 0

    for i in range(2,num):
        if (num % i) == 0:
            contador += 1

    if contador == 0:
        print(f"{num} é primo!")
    else:
        print(f"{num} não é primo!")

if __name__ == '__main__':
    numeros_primos()