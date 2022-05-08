"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a.Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b.Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c.A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
que o usuário digite o salário inicial do funcionário.
"""

aumento = 0.015
ano_contratacao = 1995
ano_atual = 2000

anos_trabalhados = ano_atual - ano_contratacao

salario = float(input("Qual é o salario inicial do funcionario? "))

for i in range(anos_trabalhados):
    salario += (salario * aumento)
    aumento = aumento * 2

print(f"O salario do furionario no ano de {ano_atual} é de R${salario:.2f}")