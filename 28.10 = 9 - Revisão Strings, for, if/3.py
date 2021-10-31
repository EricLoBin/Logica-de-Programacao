'''
Faça um programa para receber um texto qualquer e só avançar para imprimir o texto se o mesmo tiver pelo menos 3 caracteres

'''

while True:
    text = input("Digite um texto com pelo menos 3 caracteres: ")
    if(len(text)>=3):
        print(text)
        break
