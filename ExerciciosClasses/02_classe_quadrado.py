"""
Classe Quadrado: Crie uma classe que modele um quadrado:
a.Atributos: Tamanho do lado
b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado():
    def __init__(self, tamanho_lado=0):
        self.tamanho_lado = tamanho_lado

    def retorna_valor_lado(self):
        return self.tamanho_lado

    def mudar_valor_lado(self, novo_lado):
        self.tamanho_lado = novo_lado
        return self.tamanho_lado

    def calcula_area(self):
        area_quadrado = self.tamanho_lado ** 2
        return area_quadrado

if __name__ == '__main__':
    quadrado = Quadrado()

    tamanho_lado = quadrado.tamanho_lado
    print(tamanho_lado)

    mudar_valor_lado = quadrado.mudar_valor_lado(5)
    print(mudar_valor_lado)

    calcula_area = quadrado.calcula_area()
    print(quadrado.calcula_area())