'''
- Crie um programa que receba (input) um valor e se esse valor for inferior a um salário mínimo informe que o salário está incorreto (ou fora da legislação)

Exemplo: 
Se informar 500 então mostrar:  Salário: False 
(Fora da legislação)
Se informar 1500 então mostrar: Salário: True 
(Dentro da legislação)

'''

sal = float(input("Valor do salário: "))

if sal >= 1100:
    print("Dentro da legislação")
else:
    print("Fora da legislação")
