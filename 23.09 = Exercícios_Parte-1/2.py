'''
Faça um programa que receba o valor do litro da gasolina e valor do litro do álcool na bomba e informe se é mais vantajoso abastecer com um ou outro combustível. Utilize a proporção de 70% do valor para o álcool.

'''

gas = float(input("Digite o valor da gasolina: "))
alc = float(input("Digite o valor do álcool: "))
print("%s vale mais a pena." %("A gasolina" if ((gas * 0.7) < alc) else "O álcool"))
