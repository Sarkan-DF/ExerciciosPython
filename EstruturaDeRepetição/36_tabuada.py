"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""


def tabuada():
    tabuada_de = int(input("Digite o numero da tabuada que deseja: "))
    numero_inicial = int(input("Digite o numero inicial: "))
    numero_final = int(input("Digite o numero final: "))

    while numero_inicial > numero_final:
        print("O numero inicial tem que ser menor que o numero final!")
        print("Favor digitar novamente: ")
        tabuada_de = int(input("Digite o numero da tabuada que deseja: "))
        numero_inicial = int(input("Digite o numero inicial: "))
        numero_final = int(input("Digite o numero final: "))

    for i in range(numero_inicial, numero_final+1):
        resultado = tabuada_de * i
        print(f"{tabuada_de} X {i} = {resultado}")


if __name__ == '__main__':
    tabuada()
