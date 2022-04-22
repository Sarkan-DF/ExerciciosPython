"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""
import statistics


def analize_temperaturas():
    lista_temperaturas = []
    nova_temperatura = "S"

    while nova_temperatura == "S":
        temperatura = float(input("Digita a temperatura: "))
        lista_temperaturas.append(temperatura)

        nova_temperatura = str(input("Deseja inserir uma nova temperatura? 'S' para sim e 'N' para nao: "))
        nova_temperatura = nova_temperatura.upper()

    max_temp = max(lista_temperaturas)
    min_temp = min(lista_temperaturas)
    media = statistics.mean(lista_temperaturas)
    return max_temp, min_temp, media


if __name__ == '__main__':
    maior_temp, menor_temp, media_temp = analize_temperaturas()
    print(f"A maior temperatura é {maior_temp} graus!")
    print(f"A menor temperatura é {menor_temp} graus!")
    print(f"A media das temperaturas é {media_temp} graus!")