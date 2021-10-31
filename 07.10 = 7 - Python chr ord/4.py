'''
Faça um programa para descriptografar uma frase criptografada com a cifra de César com deslocamento de 2 (duas) casas, ou seja, um programa que faça a decodificação daquilo gerado pelo exemplo do tutorial.

'''

inp = input("Digite algo para ser descriptografado: ")

string = ""
for i in inp:
    char = ord(i) - 2
    string += chr(char)

print(string)
