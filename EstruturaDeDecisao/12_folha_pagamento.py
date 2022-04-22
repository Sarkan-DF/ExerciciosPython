# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

horas_trabalhadas = float(input("Quantas horas trabalhou este mes: "))
valor_hora = float(input("Quanto ganha por hora: "))

salario_bruto = horas_trabalhadas * valor_hora
sindicato = (salario_bruto * 3) / 100
inss = (salario_bruto * 10) / 100
fgts = (salario_bruto * 11) / 100

if salario_bruto <= 900.0:
    ir = (salario_bruto * 0) / 100
    percentagem_ir = "0%"
elif salario_bruto <= 1500.0:
    ir = (salario_bruto * 5) / 100
    percentagem_ir = "5%"
elif salario_bruto <= 2500.0:
    ir = (salario_bruto * 10) / 100
    percentagem_ir = "10%"
else:
    ir = (salario_bruto * 20) / 100
    percentagem_ir = "20%"

descontos = sindicato + inss + ir
salario_liquido = salario_bruto - descontos

print(f"Salário Bruto: ({horas_trabalhadas:.0f} * {valor_hora:.0f})       : R$ {salario_bruto:.2f}")
print(f"(-) Sindicato (3%)              : R$ {sindicato:.2f}")
print(f"(-) IR ({percentagem_ir})                     : R$ {ir:.2f}")
print(f"(-) INSS (10%)                  : R$ {inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {descontos:.2f}")
print(f"Salário Liquido                 : R$ {salario_liquido:.2f}")