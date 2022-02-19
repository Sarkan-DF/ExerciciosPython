"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
def quantas_consoantes():
    letras = []
    consoantes = []
    contador = 0
    for _ in range(5):
        letras.append(str(input("Digite um letra: ")))
    for i in letras:
        if i not in ("a", "e", "i", "o", "u"):
            consoantes.append(i)
            contador += 1
    return consoantes, contador

if __name__ == '__main__':
    consoantes, contador = quantas_consoantes()
    consoantes = ", ".join(consoantes)
    print(f"Foram digitadas {contador} consoantes que são {consoantes}.")