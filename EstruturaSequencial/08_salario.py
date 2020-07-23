# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganha_por_hora = float(input("Quanto ganha por hora: "))
horas_por_mes = float(input("Quantas horas trabalhou este mes: "))
salario = ganha_por_hora * horas_por_mes
print(f"Seu salario este mes é: R${salario:.2f}")