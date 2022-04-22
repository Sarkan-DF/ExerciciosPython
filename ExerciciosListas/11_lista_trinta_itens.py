"""Faça um Programa que leia 3 vetores com 10 elementos cada. Gere um terceiro vetor de 30 elementos, cujos valores
 deverão ser compostos pelos elementos intercalados dos 3 outros vetores.
"""

def lista_vinte_itens():
    lista_1 = [1,4,7,10,13,16,19,22,25,28]
    lista_2 = [2,5,8,11,14,17,20,23,26,29]
    lista_3 = [3,6,9,12,15,18,21,24,27,30]
    lista_4 = []
    for i, x, y in zip(lista_1, lista_2, lista_3):
        num_1, num_2, num_3 = i, x, y
        lista_4.append(num_1)
        lista_4.append(num_2)
        lista_4.append(num_3)

    return lista_4

if __name__ == '__main__':
    print(lista_vinte_itens())