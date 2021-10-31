'''
- Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo), depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não. 
    * A escola aceita notas 7 (sete) acima para aprovação.
    * Atenção para a indentação do código (inclusive na entrega dos exercícios)

n1 = int(input(“Nota-1: “))
if n1 < 0 or n1 > 10:
   # inválido
else:
    n2 …
    if n2 < 0 or n2 > 10:
         print (“Inválido”)
    else:
          n3 …

'''

def receberNota(num):
    nota = float(input("-=+=-\nDigite a %sª nota: " %(num)))
    if (0 <= nota <= 10):
        return nota
    else:
        return receberNota(num)


n1, n2, n3 = receberNota(1), receberNota(2), receberNota(3)

media = (n1 + n2 + n3)/3

print("--==+=--\n %s com média: %s"%("Aprovado" if (media >= 7) else "Reprovado", media))
