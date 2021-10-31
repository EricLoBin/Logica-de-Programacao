'''
Faça três programas para que as entradas (input - sempre String) de dados dos exemplos tenham as saídas propostas. Deve ser genérico.

Segundo:
# ABC -> A+B+C
# 1234 -> 1+2+3+4
# PYTHON -> P+Y+T+H+O+N

'''

str = input("Digite algo: ")

finalStr = ""

for char in str:
    finalStr = finalStr + char + "+"

print(finalStr[0:(len(finalStr)-1)])
