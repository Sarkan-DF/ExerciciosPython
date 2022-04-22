# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Digite o peso do peixe: "))
peso_maximo = 50.0
multa_por_quilo = 4.0

if peso_peixe > peso_maximo:
    excesso = peso_peixe - peso_maximo
    multa = excesso * multa_por_quilo
    print(f"Neste peixe houve excesso de {excesso:.1f}Kg com multa de R${multa:.2f}.")
else:
    print("Não houve excesso de pesso no peixe.")