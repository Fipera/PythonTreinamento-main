from tkinter import *
from tkinter import messagebox

tela = Tk()

tela.geometry("950x400")
tela.title("Entry - Campos de entrada de dados")

usuario = Label(text = "Usuario: ", font = "Arial 40")
usuario.grid(row=1, column=0, stick = "W")

campoUsuario = Entry(font = "Arial 40")
campoUsuario.grid(row=1, column= 1, stick ="W")

senha = Label(text = "Senha: ", font = "Arial 40")
senha.grid(row=2, column=0, stick = "W")

campoSenha = Entry(font = "Arial 40", show = "*")
campoSenha.grid(row=2, column= 1, stick ="W")

def logar():

    nome = str(campoUsuario.get())
    senha = str(campoSenha.get())

    if nome == "steven" and senha == "555":
        messagebox.showinfo("Messagem", "Bem vindo ao sistema!")
    else:
        messagebox.showinfo("Messagem", "Usúario ou a senha são inválidos!")

botao = Button(text = "ENTRAR",
               font = "Arial 40",
               command= logar)

botao.grid(row=3, column=0, columnspan = 2, stick="NSEW")

tela.mainloop()