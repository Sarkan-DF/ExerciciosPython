"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
a.$200 - $299
b.$300 - $399
c.$400 - $499
d.$500 - $599
e.$600 - $699
f.$700 - $799
g.$800 - $899
h.$900 - $999
i.$1000 em diante
"""


def comissao_vendedores(semanas_trabalhadas: int, vendas_brutas: float):
    comissao = (vendas_brutas * 9 / 100)
    salario_liquido = (200 * semanas_trabalhadas) + comissao
    return salario_liquido


if __name__ == '__main__':
    lista_funcinonario = [[2, 2000.00], [3, 1500.00], [1, 1000.00], [2, 3000.00], [2, 1000.00]]
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    contador_4 = 0
    contador_5 = 0
    contador_6 = 0
    contador_7 = 0
    contador_8 = 0
    contador_9 = 0

    for i in lista_funcinonario:
        semanas_trabalhadas, vendas_brutas = i
        salario_liquido = comissao_vendedores(semanas_trabalhadas, vendas_brutas)
        print(salario_liquido)
        if 200 <= salario_liquido <= 299:
            contador_1 += 1
        elif 300 <= salario_liquido <= 399:
            contador_2 += 1
        elif 400 <= salario_liquido <= 499:
            contador_3 += 1
        elif 500 <= salario_liquido <= 599:
            contador_4 += 1
        elif 600 <= salario_liquido <= 699:
            contador_5 += 1
        elif 700 <= salario_liquido <= 799:
            contador_6 += 1
        elif 800 <= salario_liquido <= 899:
            contador_7 += 1
        elif 900 <= salario_liquido <= 999:
            contador_8 += 1
        elif salario_liquido > 1000:
            contador_9 += 1

    print("Lista de fucionarios que recebem:\n"
          f"$200 - $299: {contador_1} funcionario(s)\n"
          f"$300 - $399: {contador_2} funcionario(s)\n"
          f"$400 - $499: {contador_3} funcionario(s)\n"
          f"$500 - $599: {contador_4} funcionario(s)\n"
          f"$600 - $699: {contador_5} funcionario(s)\n"
          f"$700 - $799: {contador_6} funcionario(s)\n"
          f"$800 - $899: {contador_7} funcionario(s)\n"
          f"$900 - $999: {contador_8} funcionario(s)\n"
          f"$1000 acima: {contador_9} funcionario(s)\n")