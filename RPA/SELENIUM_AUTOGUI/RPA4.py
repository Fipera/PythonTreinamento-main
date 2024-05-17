import xlsxwriter 
import os

caminhoArquivo = "C:\\Users\\Win7\\Desktop\\Documents\\salvar valores excel 1\\Dolar e Euro google.xlsx"
planilha = xlsxwriter.Workbook(caminhoArquivo)
planilha1 = planilha.add_worksheet()

planilha1.write("A1", "Nome")
planilha1.write("B1", "Idade")
planilha1.write("A2", "Amanda")
planilha1.write("B2", 28)
planilha1.write("A3", "Roberto")
planilha1.write("B3", 24)

planilha.close()

os.startfile(caminhoArquivo)

