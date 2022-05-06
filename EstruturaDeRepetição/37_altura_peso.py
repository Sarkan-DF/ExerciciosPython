"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""


def altura_peso():
    codigo = 1
    lista_dados = []
    lista_dados2 = []
    while codigo != 0:
        codigo = int(input("Qual o seu codigo? "))
        if codigo == 0:
            break
        peso = int(input("Qual o seu peso? "))
        altura = float(input("Qual a seu altura? "))
        print()
        lista_dados.append(codigo)
        lista_dados.append(peso)
        lista_dados.append(altura)
        lista_dados2.append(lista_dados)
        lista_dados = []

    return lista_dados2


lista_dados = altura_peso()

def mais_alto():
    lista_dados2 = []
    for i in lista_dados:
        lista_dados2.append(i[2])
    mais_alto = max(lista_dados2)

    posicao = lista_dados2.index(mais_alto)
    codigo_mais_alto = (lista_dados[posicao][0])
    print(f"O aluno mais alto é o codigo {codigo_mais_alto} e tem {mais_alto:.2f}m de altura.")


def mais_baixo():
    lista_dados2 = []
    for i in lista_dados:
        lista_dados2.append(i[2])
    mais_baixo = min(lista_dados2)

    posicao = lista_dados2.index(mais_baixo)
    codigo_mais_baixo = (lista_dados[posicao][0])
    print(f"O aluno mais alto é o codigo {codigo_mais_baixo} e tem {mais_baixo:.2f}m de altura.")


def mais_pesado():
    lista_dados2 = []
    for i in lista_dados:
        lista_dados2.append(i[1])
    mais_pesado = max(lista_dados2)

    posicao = lista_dados2.index(mais_pesado)
    codigo_mais_pesado = (lista_dados[posicao][0])
    print(f"O aluno mais pesado é o codigo {codigo_mais_pesado} e pesa {mais_pesado}Kg.")


def mais_leve():
    lista_dados2 = []
    for i in lista_dados:
        lista_dados2.append(i[1])
    mais_leve = min(lista_dados2)

    posicao = lista_dados2.index(mais_leve)
    codigo_mais_leve = (lista_dados[posicao][0])
    print(f"O aluno mais leve é o codigo {codigo_mais_leve} e pesa {mais_leve}Kg.")


if __name__ == '__main__':
    mais_pesado()
    mais_leve()
    mais_alto()
    mais_baixo()
