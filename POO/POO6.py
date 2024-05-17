class Impressora:
    def imprimir(self, dado):

        if isinstance(dado, str):
            print(f"é um texto: {dado}")

        elif isinstance(dado, list):
            print(f"é uma lista:")
            for i in dado:
                print(f"- {i}")
        
        elif isinstance(dado, dict):
            print(f"é um dicionario")
            
            for chave, valor in dado.items():
                print(f"{chave}: {valor}")

        else:

            print("Que dado é esse osh")


impressora = Impressora()
impressora.imprimir("ola")
impressora.imprimir([1, 2])
impressora.imprimir({"salve": "1", "salve2": "2"})

