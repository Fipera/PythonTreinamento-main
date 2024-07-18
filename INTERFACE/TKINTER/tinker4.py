from tkinter import *

tela = Tk()
tela.title("Tela Botões")

def exibirMensagem():
    print("Bela clickada!")

botao = Button(tela, text = "Clique aqui", command = exibirMensagem)

botao.pack()

tela.mainloop()