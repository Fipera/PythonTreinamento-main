from tkinter import *
from tkinter import messagebox
tela = Tk()
tela.title("Tela Botões")

def exibirMensagem():
    messagebox.showinfo("PARABENS", "CLICKOU")

botao = Button(tela, text = "Clique aqui", command = exibirMensagem)

botao.pack()

tela.mainloop()