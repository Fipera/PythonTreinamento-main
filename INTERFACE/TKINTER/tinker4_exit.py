from tkinter import *

tela = Tk()
tela.title("Tela Botões")

def exibirMensagem():
    print("Curso de Tkinter")

botao = Button(tela, text = "Clique aqui", command = exibirMensagem, fg = "white", bg = "green")

botaoSair = Button(tela,
                   text = "Sair",
                   fg = "white",
                   bg = "red",
                   command = tela.destroy)

botao.pack()
botaoSair.pack(side = LEFT)

tela.mainloop()