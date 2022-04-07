"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
lista_saltos = []
soma = 0.0

def salto_em_distancia():
    global soma
    for i in range(1, 6):
        salto = float(input(f"Digite o valor da {i}: "))
        lista_saltos.append(salto)
        soma += salto
        media = soma / 5
    nome = str(input("Qual nome do atleta: "))

    return lista_saltos, nome, media

if __name__ == '__main__':
    notas, nome, media = salto_em_distancia()
    print()
    print(f"Atleta: {nome}")
    print(f"Primeiro Salto: {notas[0]}m\n"
          f"Primeiro Salto: {notas[1]}m\n"
          f"Primeiro Salto: {notas[2]}m\n"
          f"Primeiro Salto: {notas[3]}m\n"
          f"Primeiro Salto: {notas[3]}m\n"
          )
    print("Resultado final: ")
    print(f"Atleta: {nome}")
    print(f"Saltos: {' - '.join(map(str, notas))}")
    print(f"Média dos saltos: {media}m")