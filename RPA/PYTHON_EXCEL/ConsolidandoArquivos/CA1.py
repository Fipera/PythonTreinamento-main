import pandas as opcoesDoPanda
import os

caminhoArquivos = r"C:\Users\Win7\Desktop\Documents\RPA\Pandas\Excel"

listaArquivos = os.listdir(caminhoArquivos)

print(listaArquivos)

listaCaminhoArquivoExcel = [caminhoArquivos + "\\" + arquivo for arquivo in listaArquivos if arquivo[-4:] == 'xlsx' ]

print("----------------")
print(listaCaminhoArquivoExcel)

dadosArquivo = opcoesDoPanda.DataFrame()

for arquivo in listaCaminhoArquivoExcel:
    dados = opcoesDoPanda.read_excel(arquivo)
    dadosArquivo = opcoesDoPanda.concat([dadosArquivo, dados])

dadosArquivo.to_excel(r"C:\Users\Win7\Desktop\Documents\RPA\Pandas\Arquivo Consolidado.xlsx")
