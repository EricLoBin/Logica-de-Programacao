'''
Faça um programa que receba três números (inteiros) e depois imprima uma saída com os números em ordem crescente.

'''

numeros = [
    int(input("Digite um numero:")),
    int(input("Digite um numero:")),
    int(input("Digite um numero:"))
]
numeros.sort()
for numero in numeros:
    print(numero)
