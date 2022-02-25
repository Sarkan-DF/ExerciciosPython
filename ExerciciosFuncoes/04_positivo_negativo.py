"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def positivo_negativo(num:int):
    if num > 0:
        return "P"
    else:
        return "N"

if __name__ == '__main__':
    print(positivo_negativo(-2))
    print(positivo_negativo(10))
    print(positivo_negativo(0))