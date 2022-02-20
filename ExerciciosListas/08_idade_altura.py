"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
 Imprima a idade e a altura na ordem inversa a ordem lida.
"""

def idade_altura():
    vetor_idade = []
    vetor_altura = []
    for i in range(3):
        idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        vetor_idade.append(idade)
        altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
        vetor_altura.append(altura)
    vetor_idade.reverse()
    vetor_altura.reverse()
    return vetor_idade, vetor_altura

if __name__ == '__main__':
    print(idade_altura())