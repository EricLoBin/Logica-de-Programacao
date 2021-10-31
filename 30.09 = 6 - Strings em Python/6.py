'''
Faça três programas para que as entradas (input - sempre String) de dados dos exemplos tenham as saídas propostas. Deve ser genérico.

Terceiro:
# ABCDEF -> FAEBDC
# 1234567890 -> 0192837465
# PYTHON -> NPOYHT
# Carlos -> sCoalr
# 1234567 -> 7162534
# VXYWZ -> ZVWXY

'''

str = input("Digite algo: ")

s = ""

for i in range(len(str)//2):
    s = s + str[len(str)-i-1]
    s = s + str[i]

if len(str) % 2 == 1:
    s = str[len(str)//2]

print(s)
