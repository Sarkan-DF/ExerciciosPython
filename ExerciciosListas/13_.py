"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

lista_resposta = []
lista_meses = []
lista_jan = []
lista_fev = []
lista_mar = []
temperatura = 0
temperatura2 = 0


for i in range(1,13):
    if i == 1:
        temperatura = float(input("Digite a temperatu do mes de Janeiro: "))
        temperatura2 += temperatura
        lista_jan.append(1)
        lista_jan.append("Janeiro")
        lista_jan.append(temperatura)
        lista_meses.append(lista_jan)
    elif i == 2:
        temperatura = float(input("Digite a temperatu do mes de Fevereiro: "))
        temperatura2 += temperatura
        lista_fev.append(2)
        lista_fev.append("Fevereiro")
        lista_fev.append(temperatura)
        lista_meses.append(lista_fev)
    elif i == 3:
        temperatura = float(input("Digite a temperatu do mes de Março: "))
        temperatura2 += temperatura
        lista_mar.append(3)
        lista_mar.append("Março")
        lista_mar.append(temperatura)
        lista_meses.append(lista_mar)

media = temperatura2 / 3

for x in lista_meses:
    if x[2] > media:
        lista_resposta.append(x)

for y in lista_resposta:
    print(f"O mes {y[0]} {y[1]} teve uma temperatura de {y[2]}º que ficou acima da {media:.2f}º do ano!")