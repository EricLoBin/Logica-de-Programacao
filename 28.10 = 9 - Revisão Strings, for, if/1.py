'''
Utilizando o programa do quadrado faça uma variação do programa para imprimir o caractere “+” nas diagonais principal e secundária.

'''

size = int(input("Tamanho: "))

for i in range(size**2):
    if ((i%size) == 0 and i != 0):
        print("")
    if ((i%(size-1)) == 0) or ((i%(size+1)) == 0):
        print("+", end="")
    else:
        print("0", end="")
