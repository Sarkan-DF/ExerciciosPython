# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
# o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
# atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input("Digite seu salario atual : "))

if salario_atual <= 280.0:
    reajuste = (salario_atual * 20) / 100
    percentual_aumento = "20%"
    salario_reajustado = salario_atual + reajuste

elif salario_atual <= 700.0:
    reajuste = (salario_atual * 15) / 100
    percentual_aumento = "15%"
    salario_reajustado = salario_atual + reajuste

elif salario_atual <= 1500.0:
    reajuste = (salario_atual * 10) / 100
    percentual_aumento = "10%"
    salario_reajustado = salario_atual + reajuste

else:
    reajuste = (salario_atual * 5) / 100
    percentual_aumento = "5%"
    salario_reajustado = salario_atual + reajuste

print(f"Salário antes do reajuste: R${salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}")
print(f"Valor do aumento: R${reajuste:.2f}")
print(f"Novo salário, após o aumento: R${salario_reajustado:.2f}")