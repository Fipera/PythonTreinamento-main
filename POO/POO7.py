class Veiculo:
    def mover(self):
        print("O veículo está se movendo")

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo")

class Barco(Veiculo):
    def mover(self):
        print("O barco está se movendo")

class Aviao(Veiculo):
    def mover(self):
        print("O avião está se movendo")


veiculo = Veiculo()
veiculo.mover()
carro = Carro()
carro.mover()
barco = Barco()
barco.mover()
aviao = Aviao()
aviao.mover()