"""
Classe Bola: Crie uma classe que modele uma bola:
a.Atributos: Cor, circunferência, material
b.Métodos: trocaCor e mostraCor
"""


class Bola():
    def __init__(self, cor="Verde", circunferencia=1.6, material="Madeira"):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostar_cor(self):
        return self.cor

    def troca_cor(self, nova_cor):
        self.cor = nova_cor
        return self.cor


if __name__ == '__main__':
    bola = Bola()
    print(bola.mostar_cor())
    print(bola.troca_cor("Azul"))
