# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

#Validando nome
nome = input("Digite seu nome: ")
tamanho = len(nome)

while tamanho < 3:
    print("Nome invalido!")
    nome = input("Digite novamente seu nome: ")
    tamanho = len(nome)
print("Nome registrado!")

#Valida idade
idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("Idade invalida!")
    idade = int(input("Digite novamente sua idade: "))
print("Idade registrada!")

#Valida salario
salario = float(input("Digite seu salario: "))

while salario < 0:
    print("Salario invalido!")
    salario = float(input("Digite novamento seu salario: "))
print("Salario registrado!")

#Valida sexo
sexo = input("Digite 'F' para Feminnino e 'M' para masculino: ")
sexo = sexo.upper()

while sexo != "F" and sexo != "M":
    print("Sexo invalido!")
    sexo = input("Digite novamente 'F' para Feminnino e 'M' para masculino: ")
    sexo = sexo.upper()
print("Sexo registrado!")

#Valida estado civil
estado_civil = input("Digite 'S' para Solteira(o) ou \n"
                     "Digite 'C' para Cadada(o) ou \n"
                     "Digite 'V' para Viuva(o) ou \n"
                     "Digite 'D' para Divorciada(o): ")
estado_civil = estado_civil.upper()

estado_civil_lista = ["S", "C", "V", "D"]

while estado_civil not in estado_civil_lista:
    print("Estado civil incoreto!")
    estado_civil = input("Digite 'S' para Solteira(o) ou \n"
                         "Digite 'C' para Cadada(o) ou \n"
                         "Digite 'V' para Viuva(o) ou \n"
                         "Digite 'D' para Divorciada(o): ")
    estado_civil = estado_civil.upper()
print("Estado civil registrado!")