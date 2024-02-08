
from tkinter import * 

class _int_ ():
    def Descobrir_imc(): #descobrir IMC

    
        nome = Rnome.get() #retorna o componente que foi digitado.
        altura = Raltura.get()
        peso = Rpeso.get()
        imc = peso / (altura * altura)

        resultado =f'''
        {nome} tem, {altura} de altura,
        pesa, {peso}, e seu IMC é {imc:.2f}'''

        imc_texto = resultado
def Application():
    app=Tk()
    app.title("IMC")
    app.geometry("300x300")
    app.configure(background="#dde")
    #anchor=ancora=posição dentro da caixa =>N, S, W(Oeste, esquerda), E(Leste, Direita); NE(Nordeste),SE,SO,NO(noroeste)  
    #                                                          COR LETRA                         COMPRIMENTO/ LARGURA
    Label(app,text="Nome completo",background="#fff",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20) 
    #            TEXTO          COR CAIXA                  POS. IN CAIXA   POS. IN APP.GEO 500X300 / TAMANHO CAIXA
    Rnome = Entry(app) #Utilizar o .place aqui faz a resposta do Rnome ser sucestível a erros
    Rnome.place(x=10,y=40,width=200,height=20)

    Label(app,text="Seu peso",background="#fff",foreground="#009",anchor=W).place(x=10,y=70,width=60,height=20) 

    Rpeso = Entry(app)
    Rpeso.place(x=10,y=100,width=50,height=20)

    Label(app,text="Sua Altura",background="#fff",foreground="#009",anchor=W).place(x=10,y=130,width=70,height=20) 

    Raltura = Entry(app)
    Raltura.place(x=10,y=160,width=50,height=20)

    botao = Button (app, text="Descubra seu IMC",command=Descobrir_imc)
    botao.place(x=100,y=200,width=120,height=50)

    app.mainloop()