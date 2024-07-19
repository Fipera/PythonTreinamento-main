from tkinter import *
from tkinter import messagebox

tela = Tk()

tela.geometry("950x400")
tela.title("Check Button")

info = Label(tela, text = "Selecione a opcao desejada",
             fg="blue", font="Arial 40").pack()

def azulClicado():
    print(varAzul.get())

def amareloClicado():
    print(varAmarelo.get())

def verdeClicado():
    print(varVerde.get())

varAzul = StringVar()
varAmarelo = StringVar()
varVerde = StringVar()

checkAzul = Checkbutton(tela, text = "Azul",
                        variable = varAzul,
                        onvalue = "Clicou na cor Azul",
                        fg = "blue",
                        font = "Arial 20",
                        offvalue = "",
                        height = 2,
                        width = 3,
                        command = azulClicado).pack()

checkAmarelo = Checkbutton(tela, text = "Amarelo",
                        variable = varAmarelo,
                        onvalue = "Clicou na cor Amarela",
                        fg = "yellow",
                        font = "Arial 20",
                        offvalue = "",
                        height = 2,
                        width = 6,
                        command = amareloClicado).pack()

checkVerde = Checkbutton(tela, text = "Verde",
                        variable = varVerde,
                        onvalue = "Clicou na cor Verde",
                        fg = "green",
                        font = "Arial 20",
                        offvalue = "",
                        height = 2,
                        width = 6,
                        command = verdeClicado).pack()

tela.mainloop()