# AÇÕES DE UMA PESSOA

class Pessoa:
    def __init__(self, nome, acordado=False, comendo=False, dirigindo=False, dormindo=True):
        self.nome = nome
        self.acordado = acordado
        self.comendo = comendo
        self.dirigindo = dirigindo
        self.dormindo = dormindo

    def acordar(self):
        if(self.acordado == False):
            print("A pessoa acordou")
            self.acordado = True
            self.dormindo = False
        else:
            print("A pessoa já está acordada")

    def comer(self):
        if(self.dirigindo == True):
            print("A pessoa não pode comer enquanto dirige")
        elif(self.dormindo == True):
            print("A pessoa não pode comer enquanto dorme")
        elif(self.comendo == True):
            print("A pessoa já está comendo")
        else:
            print("A pessoa comeu")
            self.comendo = True
        
    def parar_de_comer(self):
        if(self.comendo == True):
            print("A pessoa parou de comer")
            self.comendo = False
        else:
            print("A pessoa não está comendo")

    def dirigir(self):
        if(self.comendo == True):
            print("A pessoa não pode dirigir enquanto come")
        elif(self.dormindo == True):
            print("A pessoa não pode dirigir enquanto dorme")
        elif(self.dirigindo == True):
            print("A pessoa já está dirigindo")
        else:
            print("A pessoa começou a dirigir")
            self.dirigindo = True

    def parar_de_dirigir(self):
        if(self.dirigindo == True):
            print("A pessoa parou de dirigir")
            self.dirigindo = False
        else:
            print("A pessoa não está dirigindo")

    def dormir(self):
        if(self.comendo == True):
            print("A pessoa não pode dormir enquanto come")
        elif(self.dirigindo == True):
            print("A pessoa não pode dormir enquanto está dirigindo")
        elif(self.dormindo == True):
            print("A pessoa já está dormindo")
        else:
            print("A pessoa começou a dormir")
            self.dormindo = True
            self.acordado = False


pessoa1 = Pessoa("Carlos")
pessoa1.dormir()
pessoa1.acordar()
pessoa1.comer()
pessoa1.dirigir()
pessoa1.parar_de_comer()
pessoa1.dirigir()
pessoa1.dormir()
pessoa1.parar_de_dirigir()
pessoa1.dormir()
pessoa1.comer()
pessoa1.dirigir()

