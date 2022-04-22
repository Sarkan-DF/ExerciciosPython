# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que
# o valor seja maior que 500.

import sys

i = 0
x = 0
print(x)
y = 1

while i == 0:
    print(y)
    z = x + y
    x = y
    y = z
    if y > 600:
        sys.exit()