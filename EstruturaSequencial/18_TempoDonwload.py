# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
# arquivo usando este link (em minutos).

tamanho_arquiva_mb = float(input("Digite o tamanho do arquivo a ser baixado em MB: "))
velo_internet_mbps = float(input("Digite a velocidade da internet em MEGAS: "))

tempo_donwload_segundos = (tamanho_arquiva_mb * 10) / velo_internet_mbps

tempo_donwload_minutos = int(tempo_donwload_segundos / 60)
tempo_donwload_resto_segundos = tempo_donwload_segundos % 60

print(f"O tempo para baixar um arquivo de {tamanho_arquiva_mb:.0f}MB"
      f" numa internet de velocidade {velo_internet_mbps:.0f}MEGA"
      f" é de {tempo_donwload_minutos} minuto(s) e {tempo_donwload_resto_segundos:.0f} segundo(s).")