"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
"""

class televisao():
    def __init__(self, canal, volume=10):
        self.canal = canal
        self.volume = volume

    def mostra_canal_volume(self):
        return self.canal, self.volume

    def muda_canal(self, novo_canal):
        self.canal = novo_canal
        return self.canal

    def aumenta_volume(self):
        self.volume += 1
        return self.volume

    def diminui_volume(self):
        self.volume -= 1
        return self.volume

if __name__ == '__main__':
    canal = int(input("Qual canal gostaria de colocar na tv? "))
    while canal > 12 or canal < 2:
        canal = int(input("Canal invalido, digite um canal entre 2 e 12: "))
    televisao = televisao(canal)
    canal_tv, volume = televisao.mostra_canal_volume()
    print(f"Sua TV está no canal {canal_tv} e no volume {volume}!")
    print()

    variavel_volume = str(input("Gostaria de aumentar ou diminuir o volume 'S' para sim ou 'N' para não? "))
    variavel_volume = variavel_volume.upper()
    while variavel_volume == "S":
        aumenta_diminue_volume = str(input("Gostaria de aumento ou diminuir o volume? 'A' para aumentar e 'D' para diminuir: "))
        aumenta_diminue_volume = aumenta_diminue_volume.upper()
        if aumenta_diminue_volume == "A":
            televisao.aumenta_volume()
        else:
            televisao.diminui_volume()

        canal_tv, volume = televisao.mostra_canal_volume()
        print(f"Sua TV está no canal {canal_tv} e no volume {volume}!")

        variavel_volume = str(input("Gostaria de aumentar ou diminuir o volume novamente? 'S' para sim ou 'N' para não? "))
        variavel_volume = variavel_volume.upper()