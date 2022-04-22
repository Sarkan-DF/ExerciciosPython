# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
# não bissexto.

ano_bisexto = int(input("Digite o ano: "))

if ano_bisexto % 4 == 0 and ano_bisexto % 100 != 0:
    print("O ano digitado é bisexto!")
elif ano_bisexto % 4 != 0 and ano_bisexto % 400 != 0:
    print("O ano digitado não é bisexto!")
elif ano_bisexto % 4 != 0 and ano_bisexto % 400 ==0:
    print("O ano digitado é bisexto!")