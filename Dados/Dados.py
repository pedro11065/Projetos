"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazio".
"""
import time
import sys

nome = input("Digite o seu nome: ")

idade = input("digite sua idade: ")


def carregamento_pontos(tempo):
    for _ in range(3):
        sys.stdout.write(". ")
        sys.stdout.flush()
        time.sleep(tempo)

carregamento_pontos(0.25)

if nome and idade:
    ...
else:
    print("Desculpe, você deixou campos vazios")

    exit()

Espaços = nome.count(" ")

letras = (len(nome))

letra1 = (nome [0])

ultima = (nome [-1])

print ('')

print(f'Seu nome é {nome}.')
time.sleep(0.25)
print(f'Seu nome invertido é {(nome[::-1])}.')
time.sleep(0.25)
 
if Espaços == 1:
   
   print(f'Seu nome contém {Espaços} espaço.')

   time.sleep(0.25)

elif Espaços > 1 or Espaços == 0:
   
   print(f'Seu nome contém {Espaços} espaços.')

time.sleep(0.25) 
print(f'Seu nome tem {letras} letras.')
time.sleep(0.25)
print(f'sua primeira letra do nome é "{letra1}"')
time.sleep(0.25)
print(f'A ultima letra do seu nome é "{ultima}".')


