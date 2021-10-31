'''
Faça um programa para imprimir todo o alfabeto uma letra por linha e em cada linha deve ter 10 letras repetidas com utilização da repetição (for)

'''

for i in range(ord('a'), ord('z')+1):
    string = ""
    for j in range(10):
        string += chr(i)
    print(string)
