import pandas as pd

dataFrameDados = pd.read_excel(r"C:\Users\filip\Downloads\PythonTreinamento-main\PANDA\PandaFiles\Deletar_Linhas_Colunas.xlsx")

print(dataFrameDados)
print("\n----------------------------1-----------------------------------\n")
deletandoLinhasBranco = dataFrameDados.dropna()
print(deletandoLinhasBranco)
print("\n----------------------------2-----------------------------------\n")
#del deletandoLinhasBranco["Produto"]
#print(deletandoLinhasBranco)
print("\n----------------------------3-----------------------------------\n")
deletarDuasColunas = deletandoLinhasBranco.drop(columns=["Produto", "Data Venda"])

#axis - eixo(1 == coluna, 0 == linha)
deletarLinhas = deletarDuasColunas.drop(2, axis=0)
deletarLinhas = deletarLinhas.drop([0, 1], axis=0)
print(deletarLinhas)