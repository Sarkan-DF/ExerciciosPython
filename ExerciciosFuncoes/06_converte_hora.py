"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’
para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def conversao_hora(horas, minutos):
    if horas >= 12:
        horas = horas - 12
        periodo = "PM"
    else:
        periodo = "AM"
    return horas, minutos, periodo

if __name__ == '__main__':
    var = "S"
    while var == "S":
        horas = int(input("Favor digita a hora a ser convertida: "))
        minutos = int(input("Favor digita os minutos a serem convertidos: "))
        horas, minutos, periodo = conversao_hora(horas, minutos)
        print(f"{horas}:{minutos} {periodo}")
        var = str(input("Deseja converter mais um horario? 'S' para sim e 'N' para não: "))
        var = var.upper()

    print("")
    print("Obrigado por usar o programa de conversão de horas!")