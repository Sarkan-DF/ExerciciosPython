"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
 deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

def lista_vinte_itens():
    lista_1 = [1,3,5,7,9,11,13,15,17,19]
    lista_2 = [2,4,6,8,10,12,14,16,18,20]
    lista_3 = []
    for i, x in zip(lista_1,lista_2):
        num_1, num_2 = i, x
        lista_3.append(num_1)
        lista_3.append(num_2)

    return lista_3

if __name__ == '__main__':
    print(lista_vinte_itens())