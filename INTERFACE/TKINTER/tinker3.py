from tkinter import *

tela = Tk()
tela.title("Tela 3 x 3")

for linha in range(3):
    for coluna in range(3):

        tabela = Frame(
            master = tela,
            relief = RAISED,
            borderwidth = 1
        )
        tabela.grid(row=linha, column=coluna, padx=20, pady=20)
        label = Label(master=tabela, text = f"Linha {linha}\n Coluna {coluna}")
        label.pack()

tela.mainloop()