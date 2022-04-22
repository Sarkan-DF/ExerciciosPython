"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:
a.O total de votos computados; ok
b.Os númeos e respectivos votos de todos os jogadores que receberam votos;
c.O percentual de votos de cada um destes jogadores;
d.O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos.
O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o
cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de
um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de
exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar
a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um
arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
"""


def votacao_melhor_jogador():
    lista_votados = []
    total_de_votos = 0
    lista_votos = []
    numero_jogador = int(input("Digite o numero de 1 a 23 do melhor jogador em campo: "))

    while numero_jogador != 0:
        for i in range(1, 24):
            if numero_jogador == i:
                lista_votados.append(i)
                total_de_votos += 1
        numero_jogador = int(input("Digite o numero de 1 a 23 do melhor jogador em campo: "))

    lista_sem_repitidos = (list(dict.fromkeys(lista_votados)))

    for i in lista_sem_repitidos:
        lista_votos.append(lista_votados.count(i))

    return total_de_votos, lista_sem_repitidos, lista_votos


if __name__ == '__main__':
    contador = 0
    total_votos, lista_de_votados, lista_votos = votacao_melhor_jogador()
    total_votados = len(lista_de_votados)

    print(f"O total de votos foram: {total_votos}.")

    for i in range(total_votados):
        percentual_votos = (lista_votos[contador] / total_votos) * 100
        print(f"Jogador {lista_de_votados[contador]} teve {lista_votos[contador]} voto(s),"
              f" representando {percentual_votos}% do total.")
        contador += 1

    #Só falta o 'd'.