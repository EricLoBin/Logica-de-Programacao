'''
Faça três programas para que as entradas (input - sempre String) de dados dos exemplos tenham as saídas propostas. Deve ser genérico.

Primeiro:
# ABC -> ABBCCC
# 12345 -> 122333444455555

'''

str = input("Digite algo: ")

finalStr = ""

for char in range(len(str)):
    finalStr = finalStr + (str[char] * (char + 1))

print(finalStr)
