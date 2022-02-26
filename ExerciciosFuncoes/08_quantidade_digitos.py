"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def quantidade_digitos():
    num = 123
    num = str(num)
    digitos = len(num)
    return digitos, num

if __name__ == '__main__':
    digitos, num = quantidade_digitos()
    print(f"A quantidade de digitos no numero {num} é {digitos}.")