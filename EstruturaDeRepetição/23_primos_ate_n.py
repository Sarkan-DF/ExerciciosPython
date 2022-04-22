# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
# funcionamento, o estilo e o número de testes (divisões) executados.

ate_numero_primo = int(input("Digite o numero até aonde deseja saber se tem primos: "))
contador = 0
lista_primos = []
num_divisoes = 0

for num in range(2, ate_numero_primo+1):
    for x in range(2, num):
        num_divisoes += 1
        if num % x == 0:
            contador += 1

    if contador == 0:
        contador = 0
        lista_primos.append(num)
    else:
        contador = 0

if lista_primos == []:
    print(f"Não existem primos de 0 a {ate_numero_primo}")
else:
    lista_primos = str(lista_primos).strip('[]')
    print(f"Todos os primos de 0 a {ate_numero_primo} são {lista_primos}.")
    print(f"Foram nescesarias {num_divisoes} divisões para chegar neste resultado.")