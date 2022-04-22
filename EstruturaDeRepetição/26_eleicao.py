"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

def conta_votos():
    candidato_1 = 0
    candidato_2 = 0
    candidato_3 = 0

    total_votos = int(input("Quantos eleitos votaram? "))

    while total_votos != 0:
        voto = int(input("Em que deseja votar?\n"
                         "digite 1 para Candidato 1\n"
                         "digite 2 para Candidato 2\n"
                         "digite 3 para Candidato 3\n"
                         "Voto: "))
        if voto == 1:
            candidato_1 += 1
        elif voto == 2:
            candidato_2 += 1
        else:
            candidato_3 += 1

        total_votos -= 1

    return candidato_1, candidato_2, candidato_3

if __name__ == '__main__':
    candidato_1, candidato_2, candidato_3 = conta_votos()
    print(f"O total de votos foi:\n"
         f"{candidato_1} votos candidato 1\n"
         f"{candidato_2} votos candidato 2\n"
         f"{candidato_3} votos candidato 3")