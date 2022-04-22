# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

telefonema = int(input("Telefonou para a vítima? 1 para 2 para não: "))
local = int(input("Esteve no local do crime? 1 para 2 para não: "))
mora = int(input("Mora perto da vítima? 1 para 2 para não: "))
devia = int(input("Devia para a vítima? 1 para 2 para não: "))
trabalhou = int(input("Já trabalhou com a vítima? 1 para 2 para não: "))

contador = 0
lista_crime = [telefonema, local, mora, devia, trabalhou]
for x in lista_crime:
    if x == 1.0:
        contador += 1

if contador == 2.0:
    print("Suspeita")
elif contador >= 3.0 and contador <= 4.0:
    print("Cúmplice")
elif contador == 5.0:
    print("Assassino")
else:
    print("Inocente")