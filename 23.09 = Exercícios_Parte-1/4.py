'''
Faça um programa que receba “n” nomes via console e depois imprima esses nomes em ordem alfabética, independente de maiúsculas e minúsculas.

'''

nomes = []

while True:
    nome = input("Digite um nome (ou pressione enter para finalizar): ")
    if (nome == ""):
        break
    else:
        nomes.append(nome)

nomes.sort(key=lambda v: v.upper())

for nome in nomes:
    print(nome)
