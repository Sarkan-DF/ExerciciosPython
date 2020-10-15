# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
# calculada.

pessoas_turma = int(input("Quantas pessoas tem na turma? "))

soma_idade = 0.0
idade = 0.0

for i in range(pessoas_turma):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    soma_idade = soma_idade + idade

media_turma = soma_idade / pessoas_turma

if media_turma < 25.0:
    print(f"A media de idade da turma é {media_turma:.2f} anos.")
    print(f"A turma é jovem!")
elif media_turma < 60:
    print(f"A media de idade da turma é {media_turma:.2f} anos.")
    print(f"A turma é adulta!")
else:
    print(f"A media de idade da turma é {media_turma:.2f} anos.")
    print(f"A turma é idosa!")
