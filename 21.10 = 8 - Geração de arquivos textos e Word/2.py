'''
Crie um arquivo com algumas linhas de texto no seu editor de arquivos texto preferido (por exemplo: Bloco de Notas, Gedit, Emacs) e depois crie um programa para ler essas linhas e mostrá-las no console.

'''

file = open("temp\\text.txt", "r")

for line in file:
    print(line.replace("\n", ""))

file.close()
