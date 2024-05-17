#FRUTAS

class fruta:
    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):
        self.nome = nome
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque


def info(self):
    print(f"\n Nome da fruta: {self.nome}\n Preco por kg: {self.preco_por_kg}\n Quantidade em estoque: {self.quantidade_em_estoque}")


maca = fruta("maca", 5, 100)
banana = fruta("banana", 7, 150)


info(maca)
info(banana)