"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""


def media_alunos():
    turmas = int(input("Qual a quantidade de turmas? "))
    turmas_1 = turmas
    alunos = 0
    while turmas != 0:
        contador = int(input("Qual a quantidade de alunos desra turma? "))
        alunos += contador
        turmas -= 1
    media = alunos / turmas_1

    return alunos, turmas_1, media


if __name__ == '__main__':
    alunos, turma, media = media_alunos()
    print(f"Entre {turma} turma(s) com total de {alunos} alunos temos a media de {media} alunos.")
