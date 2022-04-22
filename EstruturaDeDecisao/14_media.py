# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
# a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

nota1 = float(input("Digite a nota do 1º sementre: "))
nota2 = float(input("Digite a nota do 2º sementre: "))

media = (nota1 + nota2) / 2

if media < 4.0:
    nota = "E"
elif media < 6.0:
    nota = "D"
elif media < 7.5:
    nota = "C"
elif media > 9.0:
    nota = "B"
else:
    nota = "A"

if (nota == "A") or (nota == "B") or (nota == "C"):
    aprovado_reprovado = "Aprovado"
else:
    aprovado_reprovado = "Reprovado"

print(f"Sua nota no 1º semestre foi {nota1} e no 2º foi {nota2} com media de {media}/{nota}"
      f" e voçe foi {aprovado_reprovado}")