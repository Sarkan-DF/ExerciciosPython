"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
   Não consegui resolver!
"""

def quatro_notas():
    notas = []
    media = 0
    for i in range(4):
        notas.append(int(input(f"Digite a {i+1}ª nota: ")))
        soma = sum(notas)
        media = soma / 4
    return notas, media

if __name__ == '__main__':
    notas, media = quatro_notas()
    notas = ", ".join(map(str, notas))
    print(f"As notas são {notas} e a media é {media}.")