# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Favor digitar uma data neste formato dd/mm/aaaa!")
dia = int(input("Favor digitar o dia com 2 digitos: "))
mes = int(input("Favor digitar o mes com 2 digitos: "))
ano = int(input("Favor digitar o ano com 4 digitos: "))
data_valida = True

#testando ano com 4 digitos
if (ano >= 9999 or ano <= 1000):
    data_valida = False

#testando mes de 1 a 12
if (mes < 0 or mes > 12):
    data_valida = False

#testando meses com 31 dias
lista_mes_31 = [1,3,5,7,8,10,12]
if mes in lista_mes_31:
    if dia < 0 or dia > 31:
        data_valida = False

#testando meses com 30 dias
lista_mes_30 = [4,6,9,11]
if mes in lista_mes_30:
    if dia < 0 or dia > 30:
        data_valida = False

#testando bisexto e fevereiro
if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0):
        if dia < 0 or dia > 29:
            data_valida = False
    elif dia < 0 or dia > 28:
        data_valida = False

#imprimindo data valida ou não
if data_valida == True:
    print("Data Valida!")
else:
    print("Data invalida!")