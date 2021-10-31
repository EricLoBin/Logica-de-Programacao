'''
- Crie uma variação do programa anterior, porém com os seguintes requisitos adicionais:
    - Calcule uma média ponderada: Peso da Nota 1 é 1, Peso da Nota 2 é 1.5 e Peso da Nota 3 é 2.
    - Ao invés de mostrar se o aluno foi aprovado ou não com base na média ponderada mostre uma menção de SR, II, MI, MM, MS ou SS, conforme a média ponderada e usando a escala:

    SR - 0
    II - < 2
    MI - < 5
    MM - < 7
    MS - < 9
    SS - >=9

'''

def receberNota(num):
    nota = float(input("-=+=-\nDigite a %sª nota: " %(num)))
    if (0 <= nota <= 10):
        return nota
    else:
        return receberNota(num)


n1, n2, n3 = receberNota(1), receberNota(2), receberNota(3)

media = (n1 + n2 + n3)/3

if (media == 0):
    print("SR")
elif (media < 2):
    print("II")
elif (media < 5):
    print("MI")
elif (media < 7):
    print("MM")
elif (media < 9):
    print("MS")
else:
    print("SS")
