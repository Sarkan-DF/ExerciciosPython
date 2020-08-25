# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))
operacao = float(input("Que operação deseja fazer?"
                       " '1' para somar, '2' para subtrair, '3' para multiplicar e '4' para dividir: "))

#Valida a operação e tem o resultado da operação
operacao_validas = [1.0, 2.0, 3.0, 4.0]
if operacao in operacao_validas:
    print("Operação valida!")
    if operacao == 1.0:
        resultado = numero1 + numero2
    if operacao == 2.0:
        resultado = numero1 - numero2
    if operacao == 3.0:
        resultado = numero1 * numero2
    if operacao == 4.0:
        resultado = numero1 / numero2
else:
    print("Operação invalida")

#Par ou impar
if resultado % 2.0 == 0.0:
    par_impar = "par"
else:
    par_impar = "impar"

#Positivo ou negativo:
if resultado < 0.0:
    positivo_negativo = "negativo"
else:
    positivo_negativo = "positivo"

#Inteiro ou decimal
nunero_aredondado = round(resultado)
if resultado == nunero_aredondado:
    inteiro_decimal = "inteiro"
else:
    inteiro_decimal = "decimal"

print(f"O numero {resultado} é {par_impar}, {positivo_negativo} e {inteiro_decimal}")