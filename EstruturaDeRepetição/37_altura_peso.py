"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""


class AlturaPeso:
    def __init__(self):
        pass

    def altura_peso(self):
        codigo = 1
        lista_dados = []
        lista_dados2 = []
        while codigo != 0:
            codigo = int(input("Qual o seu codigo? "))
            if codigo == 0:
                break
            peso = int(input("Qual o seu peso? "))
            altura = float(input("Qual a seu altura? "))
            lista_dados.append(codigo)
            lista_dados.append(peso)
            lista_dados.append(altura)
            lista_dados2.append(lista_dados)
            lista_dados = []

        return lista_dados2

    def mais_pesado(self):
        lista_dados = altura_peso.altura_peso()
        lista_dados2 = []
        for i in lista_dados:
            lista_dados2.append(i[1])
        mais_pesado = max(lista_dados2)

        print(lista_dados2)
        posicao = lista_dados2.index(mais_pesado)
        codigo_mais_pesado = (lista_dados[posicao][0])
        print(f"O aluno mais pesado é o codigo {codigo_mais_pesado} e pesa {mais_pesado}Kg.")

if __name__ == '__main__':
    altura_peso = AlturaPeso()
    altura_peso.mais_pesado()