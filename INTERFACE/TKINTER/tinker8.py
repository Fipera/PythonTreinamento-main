from tkinter import *
from tkinter import messagebox

tela = Tk()

tela.geometry("500x300")
tela.title("Radio Button")

variavelOpSelecionada = StringVar(tela, "0")

def imprimirItem():
    labelResultado.config(text="Você selecionou a letra " + variavelOpSelecionada.get())

radioButtonA = Radiobutton(tela,
                           text="Letra A",
                           font = "30",
                           variable = variavelOpSelecionada,
                           value="A",
                           command=imprimirItem)

radioButtonA.pack()


radioButtonB = Radiobutton(tela,
                           text="Letra B",
                           font = "30",
                           variable = variavelOpSelecionada,
                           value="B",
                           command=imprimirItem)

radioButtonB.pack()


radioButtonC = Radiobutton(tela,
                           text="Letra C",
                           font = "30",
                           variable = variavelOpSelecionada,
                           value="C",
                           command=imprimirItem)

radioButtonC.pack()


labelResultado = Label(tela, text="", font="30")
labelResultado.pack()


tela.mainloop()