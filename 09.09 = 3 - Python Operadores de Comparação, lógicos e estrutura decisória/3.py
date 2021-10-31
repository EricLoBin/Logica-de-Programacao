'''
- Faça um programa que mostre os resultados da tabela verdade para os operadores “ou” e “não”, usando print, da mesma forma que fizemos com o “e” nesse tutorial. Podem usar o formato abaixo:

Ex: print (True, "e", True, "=", (True and True))

Quatro prints para or e dois prints para not

'''

print('''-= OR =-
%s ou %s = %s
%s ou %s = %s
%s ou %s = %s
%s ou %s = %s
-=|=-\n'''
%(True, True, (True or True),
  True, False, (True or False),
  False, True, (False or True),
  False, False, (False or False))
)

print('''-= NOT =-
não %s = %s
não %s = %s
-=|=-\n'''
%(True, (not True),
  False, (not False))
)
