'''
Exercício-2:

- Faça um programa que receba os parâmetros necessários para a obtenção e impressão do IMC. 
- Referência: http://www.calculoimc.com.br/como-calcular/

Entrada: (inputs)
Qual o seu peso? 80

'''

kg = float(input("Peso em Kg: "))
m = float(input("Altura em metros: "))
m **= 2
print("IMC: {:.2f}".format(kg/m))
