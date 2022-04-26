"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de
1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""


def tabela_pao():
    preco_cliente = float(input("Qual será o valor do paozinho? "))
    cont = 1
    print("Panificadora Pão de Ontem - Tabela de preços")
    while cont <= 50:
        preco = preco_cliente * cont
        print(f"{cont} - R${preco:.2f}.")
        cont += 1
        preco = preco_cliente


if __name__ == '__main__':
    print(tabela_pao())
