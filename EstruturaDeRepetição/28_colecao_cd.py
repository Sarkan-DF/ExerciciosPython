"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""


def calcula_colecao():
    quant_cd = int(input("Quantos CDs tem na coleção? "))
    cont_quant_cd = quant_cd
    cont_valor_cd = 0
    while quant_cd != 0:
        valor_cd = float(input("Qual valor do CD? "))
        cont_valor_cd += valor_cd
        quant_cd -= 1

    media = cont_valor_cd / cont_quant_cd
    return media


if __name__ == '__main__':
    media = calcula_colecao()
    print(f"A media de valor da sua coleção de CDs é R${media:.2f}.")
