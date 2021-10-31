'''
Exercício-1:

- Receba (input) uma base e uma altura e calcule/mostre a área de um triângulo

- Receba (input) um valor em real (R$) e mostre a conversão para dólar e euro
  Entrada -> reais (R$)
  Saída -> dolar (USD) e Euro

- Receba (input) o valor de um salário e mostre o quanto deve ser depositado de FGTS (8% do valor salário) para este salário informado

  fgts = salario * 0.08

'''

b = float(input("Base: "))
a = float(input("Altura: "))

r = (b*a)/2

print(r)

#-------------------------------------

r = float(input("Valor em Reais: R$ "))

print('Dólar: $ {:.2f}\nEuro: € {:.2f}'.format(r/5.18, r/6.16))

#-------------------------------------

s = float(input("Salário: "))

print('Valor do depósito do FGTS {:.2f}'.format(s * 0.08))
