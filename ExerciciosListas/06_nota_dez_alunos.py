"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

def quatro_nota():
    media = 0
    lista_media = []
    contador = 0

    for i in range(2):
        for x in range(4):
            nota = int(input(f"Digite as notas do aluno {i+1}: "))
            media = media + nota
            if x == 3:
                media = media / 4
                if media >= 7:
                    lista_media.append(media)
                    contador += 1
        media = 0
        print()
    return lista_media, contador

if __name__ == '__main__':
    media, alunos_aprovados = quatro_nota()
    media = ", ".join(map(str, media))
    print(f"As medias dos alunos aprovados são {media} e foram aprovados {alunos_aprovados} alunos.")