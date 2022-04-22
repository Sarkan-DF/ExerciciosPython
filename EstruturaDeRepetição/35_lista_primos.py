"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.
"""


def primos_lista():
    lista_primos = []
    contador = 0
    primo_ate = int(input("Digite o numero até onde quer verificar se é primo: "))
    for i in range(2, primo_ate+1):
        for x in range(2, i):
            if (i % x) == 0:
                contador += 1

        if contador == 0:
            contador = 0
            lista_primos.append(i)
        else:
            contador = 0
    return lista_primos, primo_ate

if __name__ == '__main__':
    lista_primo, primo_ate = primos_lista()
    print(f"O numeros primos entre 0 e {primo_ate} são: {', '.join(map(str, lista_primo))}.")