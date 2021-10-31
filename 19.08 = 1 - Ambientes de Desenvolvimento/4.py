'''
Exercício-4:

- Crie um programa que receba um nome e imprima em seguida: 
- Seja bem vindo ao Python [ nome ] !

Para receber o nome: nome = input(“Qual o nome?”)

- Crie um programa que receba um número e imprima em seguida o dobro desse número
    - Para receber um número é necessário usar a instrução/função float para transformar a entrada “input” em um número real, por exemplo: 
      numero = float(input(“Qual o número? “))

'''

nome = input("Qual o nome? ")
print("Seja bem vindo ao Python " + nome)

num = float(input("Qual o número? "))
print(num*2)
