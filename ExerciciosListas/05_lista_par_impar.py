"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

def vetor_par_impar():
    vetor_inteiro = []
    vetor_par = []
    vetor_impar = []
    for i in range(20):
        vetor_inteiro.append(i)

    for i in vetor_inteiro:
        if (i % 2) == 0:
            vetor_par.append(i)
        else:
            vetor_impar.append(i)
    return vetor_inteiro, vetor_par, vetor_impar



if __name__ == '__main__':
    vetor_inteiro, vetor_par, vetor_impar = vetor_par_impar()
    vetor_inteiro = ", ".join(map(str, vetor_inteiro))
    vetor_par = ", ".join(map(str, vetor_par))
    vetor_impar = ", ".join(map(str, vetor_impar))
    print(f"Toda a lista: {vetor_inteiro}.\nSó pares: {vetor_par}.\nSó Impares: {vetor_impar}.")