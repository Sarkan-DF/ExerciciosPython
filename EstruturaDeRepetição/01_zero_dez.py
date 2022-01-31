# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

while True:
  try:
    numero = int(input("Digite um numero de 0 a 10: "))
  except ValueError:
    print("Deve ser fornecido um valor inteiro!")
  else:
    if numero >= 0 and numero <=10:
      print(f"Numero correto: {numero}!")
      break
    else:
      print("O numero tem que ser de 0 a 10!")
