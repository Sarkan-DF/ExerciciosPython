from loja_tinta2.loja_tinta2 import LojaTitas

area_ha_ser_pintada = float(input("Digite a area a ser pintada: "))
objeto_compra = LojaTitas(area_ha_ser_pintada)

quantidade_so_latas = (objeto_compra.quantidade_e_valor_so_latas()[0])
valor_so_latas = (objeto_compra.quantidade_e_valor_so_latas()[1])
print(f"Só com latas serão {quantidade_so_latas} latas no valor de R${valor_so_latas:.2f}")

quantidade_so_galoes = (objeto_compra.quantidade_e_valor_so_galoes()[0])
valor_so_galoes = (objeto_compra.quantidade_e_valor_so_galoes()[1])
print(f"Só com galoes serão {quantidade_so_galoes} galoes no valor de R${valor_so_galoes:.2f}")

quantidade_misturada_lata = (objeto_compra.quantidade_misturada_latas_galoes_e_valor()[0])
quantidade_misturada_galao = (objeto_compra.quantidade_misturada_latas_galoes_e_valor()[1])
valor_misturado_total = (objeto_compra.quantidade_misturada_latas_galoes_e_valor()[2])
print(f"Com latas e galoes serão {quantidade_misturada_lata} lata(s) e {quantidade_misturada_galao:.0f} galoes no valor"
      f" de R${valor_misturado_total:.2f}")

menor = (objeto_compra.melhor_opcao_de_valor()[0])
produto = (objeto_compra.melhor_opcao_de_valor()[1])
print(f"A melhor opção de compra seria {produto} no valor de R${menor:.2f}")