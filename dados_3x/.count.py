#qual a letra apareceu mais nessa frase
while True:

    frase = 'O python é uma linguagem de programação. ' \
    '; multiparadigma. ' \
    '; Python foi criado por Guido Van Rossum.'

    print(frase)
    print('')

    l = None

    letra = input("Qual letra você quer saber a quantidade? ")
    print('')

    letras_validas = None

    try:
       
       l=str(letra)

       letras_validas = True
       
    except:

       letras_validas = None
        
    if letras_validas is None :
        
        print ("Erro: Letra inválida.")
        continue





    letras_permitidas = 'abcdefghijklmnopqrstuvwxyz. '


    if letra not in letras_permitidas :
       
        print("Caracter Inválido.")
        continue

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    print(frase.count(letra))
    print('')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break



