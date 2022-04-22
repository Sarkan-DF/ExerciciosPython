"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
def lista_numeros_inteiro():
    numeros_inteiros = []
    for _ in range(5):
        numeros_inteiros.append(int(input("Digite um numero inteiro: ")))
    return numeros_inteiros

if __name__ == '__main__':
    numeros_inteiros = lista_numeros_inteiro()
    numeros_inteiros = ", ".join(map(str, numeros_inteiros))
    print(f"{numeros_inteiros}.")