"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

def lista_de_numeros_reais():
    numeros_reais = []
    for _ in range(3):
        numeros_reais.append(float(input("Digite um numero real: ")))
        numeros_reais.sort(reverse=True)
    return numeros_reais

if __name__ == '__main__':
    numeros_reais = lista_de_numeros_reais()
    numeros_reais = ", ".join(map(str, numeros_reais))
    print(f"{numeros_reais}.")