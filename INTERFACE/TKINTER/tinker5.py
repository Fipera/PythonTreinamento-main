from tkinter import *
from PIL import ImageTk, Image # IMAGENS
from tkinter import messagebox

tela = Tk()
tela.title("Botões com Imagem")

Label(tela, text = "Imagem",
      font = ("Verdana", 15)).pack()

# IMAGEM DE SAIR:

pathImg = ImageTk.PhotoImage(Image.open("C:\\Users\\filip\\Downloads\\PythonTreinamento-main\\INTERFACE\\TKINTER\\SAIR_tinker5.jpg"))

botaoImagem = Button(text = "Clique Aqui",
                     image = pathImg,
                     command = tela.destroy).pack()
                     

# IMAGEM DE PLANO DE FUNDO:

pathImgFundo = ImageTk.PhotoImage(Image.open("C:\\Users\\filip\\Downloads\\PythonTreinamento-main\\INTERFACE\\TKINTER\\plano_fundo_tinker5.png"))
tela.geometry("460x260")

labelFundo = Label(image = pathImgFundo)
labelFundo.place(x=0, y=0)

rotulo1 = Label(tela, text = "Python", relief=FLAT, bg ="green", fg="yellow").pack()
rotulo2 = Label(tela, text = "Python", relief=RAISED, bg ="blue", fg="white", font="Times 40 bold").pack()
rotulo3 = Label(tela, text = "Python", relief=GROOVE, bg ="purple", fg="white", font="Arial 50", borderwidth=25).pack()


tela.mainloop()