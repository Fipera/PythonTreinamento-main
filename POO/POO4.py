class Musico:
    def tocar_instrumento(self):
        print("Tocando instrumento musical")

class Atleta:
    def correr(self):
        print("Correndo na pista")

class MusicoAtleta(Musico, Atleta):
    def exibir_habilidades(self):
        print("tocando instrumento e correndo")

brabo = MusicoAtleta()
brabo.tocar_instrumento()
brabo.correr()
brabo.exibir_habilidades()
