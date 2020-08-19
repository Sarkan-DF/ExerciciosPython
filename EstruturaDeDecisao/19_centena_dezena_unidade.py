# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

import math

numero = int(input("Digite um numero menor que 1000: "))
numero1 = numero

#descobrindo as centenas
centena = numero / 100
centena = math.floor(centena)
numero = numero - (centena * 100)

#descobrindo as dezenas
dezena = numero / 10
dezena = math.floor(dezena)
numero = numero - (dezena * 10)

#descobrindo as unidades
unidade = numero / 1
unidade = math.floor(unidade)
numero = numero - (unidade * 10)

if centena > 1:
    escrita_centena = "centenas"
else:
    escrita_centena = "centana"

if dezena > 1:
    escrita_dezena = "dezenas"
else:
    escrita_dezena = "dezena"

if unidade > 1:
    escrita_unidade = "unidades"
else:
    escrita_unidade = "unidade"

print(f"O numero {numero1} tem {centena} {escrita_centena}, {dezena} {escrita_dezena} e {unidade} {escrita_unidade}")