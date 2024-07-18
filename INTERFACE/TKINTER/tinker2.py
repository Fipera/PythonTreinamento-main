from tkinter import *

tela = Tk()
tela.title("Tela daora")

rotulo1 = Label(tela, text = "Python", relief=FLAT, bg ="green", fg="yellow")
rotulo2 = Label(tela, text = "Python", relief=RAISED, bg ="blue", fg="white", font="Times 40 bold")
rotulo3 = Label(tela, text = "Python", relief=SUNKEN)
rotulo4 = Label(tela, text = "Python", relief=GROOVE, bg ="purple", fg="white", font="Arial 50", borderwidth=25)
rotulo5 = Label(tela, text = "Python", relief=RIDGE)
rotulo1.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()

tela.mainloop()