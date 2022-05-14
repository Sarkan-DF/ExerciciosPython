"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
seguintes dados:
a.Código da cidade;
b.Número de veículos de passeio (em 1999);
c.Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e.Qual a média de veículos nas cinco cidades juntas;
f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
import statistics

lista_cidades = []
cidade1 = [115, 2500, 150]
cidade2 = [25, 1808, 130]
cidade3 = [13, 1500, 110]
cidade4 = [25, 2600, 180]
cidade5 = [45, 1200, 80]

lista_cidades.append(cidade1)
lista_cidades.append(cidade2)
lista_cidades.append(cidade3)
lista_cidades.append(cidade4)
lista_cidades.append(cidade5)


def maior_ind_acidentes():
    lista_cidades2 = []
    for i in lista_cidades:
        lista_cidades2.append(i[2])
    maior = max(lista_cidades2)
    posicao = lista_cidades2.index(maior)
    codigo_maior = lista_cidades[posicao][0]
    return maior, codigo_maior


def menor_ind_acidentes():
    lista_cidades2 = []
    for i in lista_cidades:
        lista_cidades2.append(i[2])
    menor = min(lista_cidades2)
    posicao = lista_cidades2.index(menor)
    codigo_menor = lista_cidades[posicao][0]
    return menor, codigo_menor


def media_veiculos():
    lista_cidades2 = []
    for i in lista_cidades:
        lista_cidades2.append(i[1])
    media = statistics.mean(lista_cidades2)
    return media


def media_acidentes():
    lista_cidades2 = []
    for i in lista_cidades:
        if i[1] < 2000:
            lista_cidades2.append(i[2])
    media_acidentes = statistics.mean(lista_cidades2)
    return media_acidentes



if __name__ == '__main__':
    maior, codigo_maior = maior_ind_acidentes()
    print(f"A cidade com o maior numero de acidentes é a de codigo {codigo_maior} com {maior} acidentes com vitimas.")

    menor, codigo_menor = menor_ind_acidentes()
    print(f"A cidade com o menor numero de acidentes é a de codigo {codigo_menor} com {menor} acidentes com vitimas.")

    media = media_veiculos()
    print(f"A media de carro das 5 cidades é {media} veiculos.")

    media_acidentes = media_acidentes()
    print(f"A media de acidentes em cidades com menos de 2000 habitantes é {media_acidentes:.2f} acidentes com vitimas.")

