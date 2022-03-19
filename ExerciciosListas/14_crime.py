"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

def crime():
    contador = 0
    print("Investigação criminal: ")
    lista_perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
                       "Devia para a vítima?", "Já trabalhou com a vítima?"]

    for i in lista_perguntas:
        resposta = int(input("Favor responder 1 para sim e 2 para não? "
                             f"{i} "))
        if resposta == 1:
            contador += 1

    print(contador)
    if contador == 2:
        SUSPEITA = "Suspeito"
        return SUSPEITA
    elif contador >= 3 and contador <= 4:
        CUMPLICE = "Cúmplice"
        return CUMPLICE
    elif contador == 5:
        ASSASINO = "Assassino"
        return ASSASINO
    else:
        INOCENTE = "Inocente"
        return INOCENTE

if __name__ == '__main__':
    print(crime())