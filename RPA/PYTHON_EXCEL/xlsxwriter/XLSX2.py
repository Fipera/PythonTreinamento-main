import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\FormulasExemplo.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")





sheetDados.write('A1', 'Numero 1')
sheetDados.write('B1', 'Numero 2')
sheetDados.write('C1', 'Formula')

sheetDados.write('A2', '10')
sheetDados.write('A3', '6')
sheetDados.write('A4', '8')
sheetDados.write('A5', '6')
sheetDados.write('A8', 'Ana')

sheetDados.write('B2', 7)
sheetDados.write('B3', 5)
sheetDados.write('B4', 3)
sheetDados.write('B5', 1)
sheetDados.write('B8', 'Paula')

sheetDados.write_formula('C2', "=A2+B2")
sheetDados.write_formula('C3', "=A3-B3")
sheetDados.write_formula('C4', "=A4*B4")
sheetDados.write_formula('C5', "=A5/B5")

sheetDados.write_formula('C8', '=CONCATENATE(A8, " ",B8)')

sheetDados.set_column('A:C', 20)

minhaPlanilha.close()

os.startfile(caminhoArquivo)