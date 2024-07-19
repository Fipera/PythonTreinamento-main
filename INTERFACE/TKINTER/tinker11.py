from tkinter import *
from tkinter import messagebox


tela = Tk()

tela.geometry("500x500")
tela.title("listbox")

# textoDiaSemana = Label(tela, text="Dia da semana", font="Arial 30")
# textoDiaSemana.pack()

listaNomes = ("Ana", "Amanda", "Cesar")

variavelNomes = Variable(value=listaNomes)

listabox = Listbox(tela, 
                   listvariable = variavelNomes,
                   height=5,
                   font="Arial 40",
                   selectmode = SINGLE)

# listabox.insert(1, "Domingo")
# listabox.insert(2, "Segunda")
# listabox.insert(3, "Terça")
# listabox.insert(4, "Quarta")
# listabox.insert(5, "Quinta")
# listabox.insert(6, "Sexta")
# listabox.insert(7, "Sábado")

listabox.pack(expand = True, fill = BOTH)

def itemSelecionado(evento):

    indSelecionado = listabox.curselection()
    item = ",".join([listabox.get(posicao) for posicao in indSelecionado])
    mensagem = "Você selecionou: " + item
    messagebox.showinfo(title="Atenção", message=mensagem)

listabox.bind("<<ListboxSelect>>", itemSelecionado)

textoParaAdicionar = Entry(font = "Arial 20")
textoParaAdicionar.pack()

def adicionarItem():

    listabox.insert(END, str(textoParaAdicionar.get())) 

botaoAdicionar = Button(text="Adicionar item na lista",
                         font = "Arial 20",
                         command = adicionarItem)

botaoAdicionar.pack()

tela.mainloop()

