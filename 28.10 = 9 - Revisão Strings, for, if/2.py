'''
Faça um programa para imprimir o nome a quantidade de vezes que for o número de caracteres do nome. Exemplo:

Flavia -> 6 caracteres

Flavia
Flavia
Flavia
Flavia
Flavia
Flavia

'''

name = input("Digite seu nome: ")
print(f"{name}\n"*len(name))
