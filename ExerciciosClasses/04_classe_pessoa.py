"""
Classe Pessoa: Crie uma classe que modele uma pessoa:
a.Atributos: nome, idade, peso e altura
b.Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa():
    def __init__(self, nome="Igor", idade=35, peso=85, altura=1.80):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def mostra_dados(self):
        return self.nome, self.idade, self.peso, self.altura

    def envelhecer_crece(self, crecer=None):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

if __name__ == '__main__':
    pessoa = Pessoa("Igor", 10, 70, 1.50)
    print(f"Dado originais: {pessoa.mostra_dados()}")

    pessoa.envelhecer_crece()
    pessoa.envelhecer_crece()
    pessoa.envelhecer_crece()
    print(f"Envelhecida 3 ano: {pessoa.mostra_dados()}")

    pessoa.engordar()
    print(f"Um kilo a mais: {pessoa.mostra_dados()}")

    pessoa.emagrecer()
    print(f"Um kilo a menos: {pessoa.mostra_dados()}")
