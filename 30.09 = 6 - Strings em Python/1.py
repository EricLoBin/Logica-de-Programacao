'''
- Faça um programa que receba uma String e depois imprima a mesma frase em uma linha para cada:
    - Minúsculo
    - Maiúsculo
    - Com os caracteres “e” trocados/substituídos por “and”.

'''

str = input("Digite algo: ")
print(str.lower())
print(str.upper())
print(str.replace("e", "and"))
