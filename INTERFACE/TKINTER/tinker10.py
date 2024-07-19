from tkinter import *
from tkinter import messagebox
from tkinter import ttk

tela = Tk()

tela.geometry("700x200")
tela.title("Comobobox")

Label(tela, text= "Selecione um mês:",
      font = "Arial 18").grid(row = 1, column=0)

mesSelecionado = ttk.Combobox(tela, font = "Arial 20")

mesSelecionado["values"] = ["Janeiro", 
                            "Fevereiro", 
                            "Março", 
                            "Abril",
                            "Maio", 
                            "Junho", 
                            "Julho", 
                            "Agosto",
                            "Setembro", 
                            "Outubro", 
                            "Novembro", 
                            "Dezembro"
                            ]

mesSelecionado.grid(row = 1, column=1)
mesSelecionado.current(4)


def itemSelecionado():
    print(str(mesSelecionado.get()))



botaoSelecionar = Button(text="item selecionado",
                         font = "Arial 20",
                         command= itemSelecionado)

botaoSelecionar.grid(row = 2, column=0, columnspan=2, stick= "NSEW")


tela.mainloop()