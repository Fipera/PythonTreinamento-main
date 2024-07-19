from tkinter import *


tela = Tk()

tela.geometry("950x200")
tela.title("Entry - Campos de entrada de dados")

nome = Label(text = "Nome: ", font = "Arial 40")
nome.grid(row=1, column=0, stick = "W")

campoNome = Entry(font = "Arial 40")
campoNome.grid(row=1, column= 1, stick ="W")

sobreNome = Label(text = "Sobre Nome: ", font = "Arial 40")
sobreNome.grid(row=2, column=0, stick = "W")

campoSobreNome = Entry(font = "Arial 40")
campoSobreNome.grid(row=2, column= 1, stick ="W")

tela.mainloop()