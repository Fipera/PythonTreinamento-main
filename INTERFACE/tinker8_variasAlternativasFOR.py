from tkinter import *
from tkinter import messagebox

tela = Tk()

tela.geometry("500x900")
tela.title("Radio Button")

variavelOpSelecionada = StringVar(tela, "0")

def imprimirItem():
    labelResultado.config(text="Você selecionou a letra " + variavelOpSelecionada.get())

opcoes = {"Letra A" : "A",
          "Letra B" : "B",
          "Letra C" : "C",
          "Letra D" : "D",
          "Letra E" : "E",
          "Letra F" : "F",
          "Letra G" : "G",
          "Letra H" : "H",
          "Letra I" : "I",
          "Letra J" : "J",
          "Letra K" : "K",
          "Letra L" : "L"
          }

for(textoColuna0, textoColuna1) in opcoes.items():
    Radiobutton(tela, 
                text= textoColuna0,
                variable=variavelOpSelecionada,
                value=textoColuna1,
                font = 30,
                command = imprimirItem).pack()

          


labelResultado = Label(tela, text="", font="30")
labelResultado.pack()


tela.mainloop()