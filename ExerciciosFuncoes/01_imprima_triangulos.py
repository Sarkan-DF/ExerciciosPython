"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""

def imprima_triangolos(n: int):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end="   ")
        print("")

if __name__ == '__main__':
    imprima_triangolos(5)