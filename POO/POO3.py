#RESERVAS

class Evento:
    def __init__(self, capacidade=10):
        self.capacidade_atual = capacidade
        self.capacidade = capacidade

    def reservar(self):
        if(self.capacidade_atual > 0):
            print("1 vaga reservada")
            self.capacidade_atual -= 1
        else:
         print("Evento lotado")

    def cancelar(self):
        if(self.capacidade_atual < self.capacidade):
           print("1 vaga cancelada")
           self.capacidade_atual += 1
        else:
            print("Sem vagas para cancelar")
    
    def lugares_disponiveis(self):
        print(f"Lugares disponiveis: {self.capacidade_atual}")

evento = Evento()
evento.reservar()
evento.lugares_disponiveis()
evento.reservar()
evento.lugares_disponiveis()
evento.cancelar()
evento.lugares_disponiveis()

        
    

