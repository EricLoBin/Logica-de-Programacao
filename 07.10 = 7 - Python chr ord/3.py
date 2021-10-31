'''
Faça um programa para imprimir um triângulo com as letras do alfabeto. Utilize o for e a função chr.

A
BB
CCC
…
ZZZZZZZZZ…

'''

for i in range(ord('a'), ord('z')+1):
    print((chr(i)*((i-ord('a'))+1)).center((ord('z')-ord('a'))+1))
