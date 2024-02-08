"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Que horas são?")

try:

    hora_int = (int(hora))

    if hora_int in range(0, 11):
        print("Então bom dia!")
    elif hora_int in range(12, 17):
        print("Então Boa tarde!")
    elif hora_int in range(18, 23):
        print("Então Boa noite!")
    else:
        print("Digite um horário real!")

except: 
    print("Digite um horário real!")