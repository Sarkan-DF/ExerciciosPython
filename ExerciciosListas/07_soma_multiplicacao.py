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

if __name__ == '__main__':
    soma, multiplicacao, numeros = soma_multiplicacao()
    print(f"A soma de todos os numeros é: {soma}.")
    print(f"A multiplicação de todos os numeros é: {multiplicacao}.")
    numeros = ", ".join(map(str, numeros))
    print(f"A lista de numeros é: {numeros}.")