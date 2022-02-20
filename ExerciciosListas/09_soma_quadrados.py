"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
 do vetor.
"""

def soma_quadrados():
    lista_soma = []
    for i in range(10):
        i += 1
        quadrado = i ** 2
        lista_soma.append(quadrado)

    return lista_soma

if __name__ == '__main__':
    print(soma_quadrados())