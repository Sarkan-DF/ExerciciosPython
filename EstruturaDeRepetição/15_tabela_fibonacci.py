# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até
# o n−ésimo termo.

quantos_termos = int(input("Deseja visualizar quantos termos da tabela Fibonacci? "))

x = 0
print(x)
y = 1

for i in range(1,quantos_termos):
    print(y)
    z = x + y
    x = y
    y = z