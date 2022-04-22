# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo.

ganha_por_hora = float(input("Quanto ganha por hora: "))
horas_por_mes = float(input("Quantas horas trabalhou este mes: "))

salario_bruto = ganha_por_hora * horas_por_mes
inss = (salario_bruto / 100) * 8
ir = (salario_bruto / 100) * 11
sindicato = (salario_bruto / 100) * 5
salario_liquido = salario_bruto - (inss + sindicato + ir)

print(f"\n+ Salário Bruto   : R${salario_bruto:.2f}\n"
      f"- IR (11%)        : R${ir:.2f}\n"
      f"- INSS (8%)       : R${inss:.2f}\n"
      f"- Sindicato (5%)  : R${sindicato:.2f}\n"
      f"= Salário Liquido : R${salario_liquido:.2f}")
