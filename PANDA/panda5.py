import pandas as pd

baseVendas_DF = pd.read_excel(r"C:\Users\filip\Downloads\PythonTreinamento-main\PANDA\PandaFiles\Base_Vendas.xlsx")

resumoValoresUnicos = baseVendas_DF.nunique()
#confereDuplicidades = baseVendas_DF.duplicated(subset="Vendedor", keep='first')
baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset="Vendedor", keep='first')

print(baseVendas_DF)
print("\n--------------------------1-------------------------------------\n") 
print(resumoValoresUnicos)
#print("\n--------------------------2-------------------------------------\n")
#print(confereDuplicidades)