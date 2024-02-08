"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""
try: 
    numero = (int(input("Digite um número: ")))


    numero_int = (int(numero))

    if numero % 2 == 0:
        print(f"{numero} é par.")

    else:
        print(f"{numero} é impar.")

except:
    print(f"Esse digito não é um número inteiro.")



