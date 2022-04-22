"""
Classe Retangulo: Crie uma classe que modele um retangulo:
a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c.Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class retangulo():
    def __init__(self, ladoa=0, ladob=0):
        self.ladoa = ladoa
        self.ladob = ladob

    def valor_lados(self):
        return self.ladoa, self.ladob

    def muda_valor_lados(self, novo_valor_ladoa,novo_valor_ladob):
        self.ladoa = novo_valor_ladoa
        self.ladob = novo_valor_ladob
        return self.ladoa, self.ladob

    def calcula_area_retangulo(self):
        area_retangulo = self.ladoa * self.ladob
        return area_retangulo

    def calcula_perimetro_retangulo(self):
        perimetro_retangulo = (self.ladoa + self.ladob) * 2
        return perimetro_retangulo

if __name__ == '__main__':
    retangulo = retangulo()
    lados = retangulo.valor_lados()
    print(lados)

    novos_lados = retangulo.muda_valor_lados(5,4)
    print(novos_lados)

    area_retangulo = retangulo.calcula_area_retangulo()
    print(area_retangulo)

    perimetro_retangulo = retangulo.calcula_perimetro_retangulo()
    print(perimetro_retangulo)