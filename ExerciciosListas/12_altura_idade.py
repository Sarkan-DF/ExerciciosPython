"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
"""

def altura_media():

    lista_idade_altura = [[14, 1.80], [11, 1.70], [10, 1.60], [15, 1.70], [17, 1.88]]
    lista_maior_13 = []
    total_altura = 0
    contador_1 = 0
    alunos_abaixo_media = 0

    for i in lista_idade_altura:
        if i[0] > 13:
            lista_maior_13.append(i)

    for x in lista_idade_altura:
        contador_1 += 1
        total_altura += x[1]

    media_altura = total_altura / contador_1

    for y in lista_maior_13:
        if y[1] < media_altura:
            alunos_abaixo_media += 1


    return media_altura, alunos_abaixo_media

if __name__ == '__main__':
    media_altura, alunos_abaixo_media = altura_media()
    print(f"A quantidade de alunos com mais de 13 anos com media de altura menor que {media_altura:.2f} é de"
          f" {alunos_abaixo_media} aluno(s).")
