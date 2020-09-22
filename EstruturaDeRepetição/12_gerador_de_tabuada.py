# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
# informar de qual numero ele deseja ver a tabuada.

tabuada = int(input("Digite a tabuada que deseja gerar: "))

for x in range(1,11):
    resultado = tabuada * x
    print(f"{tabuada} x {x} = {resultado}")