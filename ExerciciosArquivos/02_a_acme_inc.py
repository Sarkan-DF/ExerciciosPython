meu_arquivo = open("C:/Users/Igor.Matos/Documents/files.txt", "w")
meu_arquivo.writelines("Curso Python Progressivo:\n")
meu_arquivo.close()

meu_arquivo = open("C:/Users/Igor.Matos/Documents/files.txt", "a")
meu_arquivo.writelines("O melhor curso de Pythom!")
meu_arquivo.close()

meu_arquivo = open("C:/Users/Igor.Matos/Documents/files.txt")
print(meu_arquivo.read())