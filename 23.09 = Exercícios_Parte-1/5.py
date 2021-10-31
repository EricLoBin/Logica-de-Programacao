'''
Faça um programa que receba um número de 1 até 99 e depois mostre esse número no console escrito por extenso.

'''

def switchCase(case):
    if (int(case) < 20):
        caseList = {
            1:"um",
            2:"dois",
            3:"três",
            4:"quatro",
            5:"cinco",
            6:"seis",
            7:"sete",
            8:"oito",
            9:"nove",
            10:"dez",
            11:"onze",
            12:"doze",
            13:"treze",
            14:"catorze",
            15:"quinze",
            16:"dezesseis",
            17:"dezessete",
            18:"dezoito",
            19:"dezenove"
        }
        return caseList[int(case)]
    else:
        caseList = {
            2:"vinte",
            3:"trinta",
            4:"quarenta",
            5:"cinquenta",
            6:"sessenta",
            7:"setenta",
            8:"oitenta",
            9:"noventa"
        }
        return caseList[int(case[0])] + ((" e " + switchCase(case[1])) if (case[1] != "0") else "")

print(switchCase(input("Digite o número de 1 a 99: ")))
