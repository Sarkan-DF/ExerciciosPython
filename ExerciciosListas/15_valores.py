"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a.Mostre a quantidade de valores que foram lidos;
b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d.Calcule e mostre a soma dos valores;
e.Calcule e mostre a média dos valores;
f.Calcule e mostre a quantidade de valores acima da média calculada;
g.Calcule e mostre a quantidade de valores abaixo de sete;
h.Encerre o programa com uma mensagem;
"""

valor = 0
lista_valor = []
while valor != -1:
    valor = int(input("Digite um valor: "))
    if valor != -1:
        lista_valor.append(valor)

# lista original
print("")
print(f"lista original: {lista_valor}")
print("")

# a.Mostre a quantidade de valores que foram lidos;
a = len(lista_valor)
print(f"a.Mostre a quantidade de valores que foram lidos:")
print(a)
print("")

# b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro:")
for i in lista_valor:
    print(f"{i}", end=" ")
print("")
print("")

# c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro:")
lista_valor.reverse()
for i in lista_valor:
    print(i)
print("")

# d.Calcule e mostre a soma dos valores;
soma = 0
for i in lista_valor:
    soma += i
print("d.Calcule e mostre a soma dos valores:")
print(soma)
print("")

# e.Calcule e mostre a média dos valores;
media = soma / a
print("e.Calcule e mostre a média dos valores:")
print(media)
print("")

# f.Calcule e mostre a quantidade de valores acima da média calculada;
contador = 0
for i in lista_valor:
    if i > media:
        contador += 1
print("f.Calcule e mostre a quantidade de valores acima da média calculada:")
print(contador)
print("")

# g.Calcule e mostre a quantidade de valores abaixo de sete;
contador1 = 0
for i in lista_valor:
    if i < 7:
        contador1 += 1
print("g.Calcule e mostre a quantidade de valores abaixo de sete:")
print(contador1)