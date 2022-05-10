"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas.
"""
lista_alunos = []
aluno1 = [1, 150]
aluno2 = [2, 160]
aluno3 = [3, 180]
aluno4 = [4, 110]
aluno5 = [5, 120]

lista_alunos.append(aluno1)
lista_alunos.append(aluno2)
lista_alunos.append(aluno3)
lista_alunos.append(aluno4)
lista_alunos.append(aluno5)


def aluno_mais_alto():
    lista_alunos2 = []
    for i in lista_alunos:
        lista_alunos2.append(i[1])
    mais_alto = max(lista_alunos2)
    posicao = lista_alunos2.index(mais_alto)
    codigo_mais_alto = (lista_alunos[posicao][0])
    return mais_alto, codigo_mais_alto

def aluno_mais_baixo():
    lista_alunos2 = []
    for i in lista_alunos:
        lista_alunos2.append(i[1])
    mais_baixo = min(lista_alunos2)
    posicao = lista_alunos2.index(mais_baixo)
    codigo_mais_baixo = (lista_alunos[posicao][0])
    return mais_baixo, codigo_mais_baixo


if __name__ == '__main__':
    altura, codigo_mais_alto = aluno_mais_alto()
    print(f"O aluno {codigo_mais_alto} é o mais alto com {altura} centimetros.")

    altura, codigo_mais_baixo = aluno_mais_baixo()
    print(f"O aluno {codigo_mais_baixo} é o mais baixo com {altura} centimetros.")