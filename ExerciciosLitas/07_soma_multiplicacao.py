"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

def soma_multiplicacao():
    soma = 0
    multiplicacao = 1
    numeros = []
    for i in range(5):
        i += 1
        soma += i
        multiplicacao = multiplicacao * i
        numeros.append(i)
    return soma, multiplicacao, numeros


soma, multiplicacao, numeros = soma_multiplicacao()
print(soma)
print(multiplicacao)
print(numeros)