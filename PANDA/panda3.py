import pandas as pd

vendas_DataFrame = pd.read_excel(r"C:\Users\filip\Downloads\PythonTreinamento-main\PANDA\PandaFiles\Vendas_Jan.xlsx")

print(vendas_DataFrame)
print("\n--------------------------1-------------------------------------\n") 
print(vendas_DataFrame.index)
print("\n--------------------------2-------------------------------------\n")
print(vendas_DataFrame.columns) 
print("\n--------------------------3-------------------------------------\n")
# 9 primeiras linhas do DF
print(vendas_DataFrame.head(9))
print("\n--------------------------4-------------------------------------\n")
# 3 ultimas linhas do DF
print(vendas_DataFrame.tail(3))
print("\n--------------------------5-------------------------------------\n")
print(vendas_DataFrame[["Vendedor", "Total Vendas"]].head())
print("\n--------------------------6-------------------------------------\n")
print(vendas_DataFrame.loc[2:7])
print("\n--------------------------7-------------------------------------\n")
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"] == "Leonardo Almeida"]
print(vendas_Leonardo_Almeida_DF)
print("\n--------------------------8-------------------------------------\n")
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]
print(vendas_Leonardo_Almeida_DF)
print("\n--------------------------9-------------------------------------\n")
print(vendas_DataFrame.shape)
print("\n--------------------------10-------------------------------------\n")