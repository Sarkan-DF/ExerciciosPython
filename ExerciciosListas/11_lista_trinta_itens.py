"""Faça um Programa que leia 3 vetores com 10 elementos cada. Gere um terceiro vetor de 30 elementos, cujos valores
 deverão ser compostos pelos elementos intercalados dos 3 outros vetores.
"""

def lista_vinte_itens():
    lista_1 = [1,4,7,10]
    lista_2 = [2,5,8,11]
    lista_3 = [3,6,9,12]
    lista_4 = []
    lista_5 = []
    for i, x, y in zip(lista_1, lista_2, lista_3):
        numero = i, x, y
        lista_4.append(numero)

    for i in lista_4:
        lista_5.append(i[0])
        lista_5.append(i[1])
        lista_5.append(i[2])


    return lista_5

if __name__ == '__main__':
    print(lista_vinte_itens())