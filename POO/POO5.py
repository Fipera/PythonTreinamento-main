class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Veiculo da marca {self.marca} e do modelo {self.modelo}")

class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):

        super().__init__(marca,modelo)
        self.cor = cor


    def exibir_info(self):
        super().exibir_info()

        print(f"cor do carro: {self.cor}")

veiculo1 = Veiculo("toyota", "corolla")
veiculo1.exibir_info()

carro1 = Carro("toyota", "corolla", "Azul")
carro1.exibir_info()
