# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o 1º lado do triangulo: "))
lado2 = float(input("Digite o 2º lado do triangulo: "))
lado3 = float(input("Digite o 3º lado do triangulo: "))

if lado1 == lado2 == lado3:
    print("Triangulo Equilátero!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo Isósceles!")
else:
    print("Triângulo Escaleno!")