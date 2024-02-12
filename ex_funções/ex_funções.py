#Crie uma função que multiplica todos os argumentos não nomeados
#retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

#Crie uma função que diga se o número é impar ou par
#retorne se o numero é impar ou par.

def par_impar(numero):
    return numero % 2 == 0 #ele é divisível por 2 ou não? (boolean)
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(5))
#1