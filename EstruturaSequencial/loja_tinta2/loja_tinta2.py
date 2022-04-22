import math


class LojaTitas:

    def __init__(self, area_ha_ser_pintada,
                 lata_pinta_metros=18 * 6,
                 galao_pinta_metros=3.6 * 6,
                 custo_lata=80.0,
                 custo_galao=25.0):
        self.__area_ha_ser_pintada = area_ha_ser_pintada
        self.__area_ha_ser_pintada *= 1.1
        self.__lata_pinta_metros = lata_pinta_metros
        self.__galao_pinta_metros = galao_pinta_metros
        self.__custo_lata = custo_lata
        self.__custo_galao = custo_galao

    def quantidade_e_valor_so_latas(self):
        quantidade_latas = math.ceil(self.__area_ha_ser_pintada / self.__lata_pinta_metros)
        valor_latas = quantidade_latas * self.__custo_lata
        self.__valor_latas = valor_latas
        return quantidade_latas, valor_latas

    def quantidade_e_valor_so_galoes(self):
        quantidade_galaos = math.ceil(self.__area_ha_ser_pintada / self.__galao_pinta_metros)
        valor_galao = quantidade_galaos * self.__custo_galao
        self.__valor_galao = valor_galao
        return quantidade_galaos, valor_galao

    def quantidade_misturada_latas_galoes_e_valor(self):
        quantidade_misturada_lata = 0
        are_ha_ser_pintada = self.__area_ha_ser_pintada

        while self.__lata_pinta_metros <= are_ha_ser_pintada:
            are_ha_ser_pintada -= self.__lata_pinta_metros
            quantidade_misturada_lata += 1

        quantidade_misturada_galao = float(math.ceil(are_ha_ser_pintada / self.__galao_pinta_metros))

        valor_misturado_latas = quantidade_misturada_lata * self.__custo_lata
        valor_misturado_galoes = quantidade_misturada_galao * self.__custo_galao
        valor_misturado_total = valor_misturado_latas + valor_misturado_galoes
        self.__valor_misturado_total = valor_misturado_total
        return quantidade_misturada_lata, quantidade_misturada_galao, valor_misturado_total

    def melhor_opcao_de_valor(self):
        valor_latas = self.__valor_latas
        valor_galao = self.__valor_galao
        valor_misturado_total = self.__valor_misturado_total

        so_latas = "só latas"
        so_galoes = "só lagoes"
        misturados = "misturar latas e galoes"

        menor = valor_latas
        produto = so_latas

        if valor_galao < menor:
            menor = valor_galao
            produto = so_galoes
        if valor_misturado_total < menor:
            menor = valor_misturado_total
            produto = misturados
        return menor, produto
