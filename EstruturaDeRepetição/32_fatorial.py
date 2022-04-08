"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""


def fatorial():
    num = int(input("Digite o numero no qual deseja o fatorial: "))
    result = 1
    lista_fatorial = []
    for i in range(num):
        i += 1
        lista_fatorial.append(i)
        result = result * i
    lista_fatorial.reverse()
    return result, num , lista_fatorial


if __name__ == '__main__':
    fatorial_num, num, lista_fatorial = fatorial()
    print(f"Fatorial de: {num}")
    print(f"{num}! = {(' . '.join(map(str, lista_fatorial)))} = {fatorial_num}")