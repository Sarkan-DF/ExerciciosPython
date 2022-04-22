"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""
def imprima_triangulos_2(n: int):
    for linhas in range(1, n + 1):
        for coluna in range(1, linhas + 1):
            print(coluna, end="   ")
        print("")

if __name__ == '__main__':
    imprima_triangulos_2(5)