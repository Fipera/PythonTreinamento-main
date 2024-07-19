from tkinter import *
from tkinter import messagebox

tela = Tk()

tela.geometry("500x900")
tela.title("Messagebox")

info = Label(tela, text="Mensagens", font = 50).pack()


def mensagemInformacao():
    messagebox.showinfo("Informação", "Bem vindo(a) ao curso de Tkinter")

def mensagemAviso():
    messagebox.showwarning("Aviso", "Você está aprendendo Tkinter!")

def mensagemErro():
    messagebox.showerror("Erro", "Erro ao carregar o sistema")

def mensagemQuestao():
    resultado = messagebox.askquestion("Questão", "Tkinter é com Python?")
    if resultado == "yes":
        print("Se quiser sim")
    else:
        print("Mentira sua!")

def mensagemOkCancelar():
    resultado = messagebox.askokcancel("Ok ou Cancelar", "Deseja continuar?")
    if resultado:
        print("Continuando...")
    else:
        print("CANCELADO")


def mensagemSimNao():
    resultado = messagebox.askyesno("Sim ou Não", "Quer procurar o valor?")
    if resultado:
        print("Procurando...")
    else:
        print("CANCELADO")

def mensagemRepetirCancelar():
    resultado = messagebox.askretrycancel("Repetir ou Cancelar", "Você deseja tentar novamente?")
    if resultado:
        mensagemRepetirCancelar()
    else:
        print("CANCELADO")

botaoInformacao = Button(text="Informacao",
                         font = "Arial 20",
                         command = mensagemInformacao).pack()

botaoAviso = Button(text="Aviso",
                         font = "Arial 20",
                         command = mensagemAviso).pack()

botaoErro = Button(text="Erro",
                         font = "Arial 20",
                         command = mensagemErro).pack()

botaoQuestao = Button(text="Questão",
                         font = "Arial 20",
                         command = mensagemQuestao).pack()

botaoOkCancelar = Button(text="Ok ou Cancelar",
                         font = "Arial 20",
                         command = mensagemOkCancelar).pack()

botaoSimNao = Button(text="Sim ou Não",
                         font = "Arial 20",
                         command = mensagemSimNao).pack()

botaoRepetirCancelar = Button(text="Repetir ou Cancelar",
                         font = "Arial 20",
                         command = mensagemRepetirCancelar).pack()




tela.mainloop()