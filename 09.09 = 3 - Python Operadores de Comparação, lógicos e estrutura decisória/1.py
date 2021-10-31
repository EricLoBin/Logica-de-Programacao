'''
- Crie um programa que receba duas notas e informe se a pessoa passou ou não. Considere que o usuário irá informar uma nota de 0 à 10 e que média a partir de 5 leva o aluno a aprovação

Exemplo: 

(5 + 7)  / 2 = 6 Aprovado: True (ou seja está aprovado)
(4 + 3) / 2 = 3.5 Aprovado: False (ou seja está reprovado)

'''

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
resu = (nota1+nota2)/2

if resu >= 5:
    print("Aprovado",resu)
else:
    print("Reprovado",resu)
