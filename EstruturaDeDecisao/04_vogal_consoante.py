# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")
letra = letra.lower()

vogais = ["a", "e", "i", "o", "u"]
consoantes = ["q", "w", "r", "t", "y", "u", "p", "s", "d", "f", "g",
              "h", "j", "k", "l", "ç", "z", "x", "c", "v", "b", "n", "m"]

if letra in vogais:
    print("É uma vogal")
elif letra in consoantes:
    print("É uma consoante")
else:
    print("Não é uma letra.")