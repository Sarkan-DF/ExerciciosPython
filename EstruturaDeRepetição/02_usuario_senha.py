# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

usuario = input("Favor digitar seu usuario: ")
senha = input("Favor digitar sua senha: ")

while usuario == senha:
    print("Usuario e senha não podem ser iguais!")
    usuario = input("Favor digitar novamente seu usuario: ")
    senha = input("Favor digitar novamente sua senha: ")

print("Login efetuado com sucesso!")