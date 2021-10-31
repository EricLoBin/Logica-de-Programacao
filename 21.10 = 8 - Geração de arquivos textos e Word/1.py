'''
Faça um programa que receba um número e gere um arquivo texto com a tabuada de multiplicação (0 até 10) do número recebido.

'''

file = open("temp\\tabuada.txt", "w")
inp = int(input("Digite um numero para obter sua tabuada: "))

file.write(f"Tabuada do {inp}")

for i in range(11):
    file.write(f"\n{inp} x {i} = {inp*i}")

file.close()
