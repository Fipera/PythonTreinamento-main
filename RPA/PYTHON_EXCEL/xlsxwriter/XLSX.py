import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\PintaFundoFonte2.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")

#corFundo = minhaPlanilha.add_format({'fg_color':'yellow'})

corFonte = minhaPlanilha.add_format()
corFonte.set_font_color('blue')

corFonteFundo = minhaPlanilha.add_format({
    'align': 'center', 
    'font_color': 'white',
    'bold': True,
    'bg_color': 'gray'
})

sheetDados.write('A1', 'Nome', corFonteFundo)
sheetDados.write('B1', 'Idade', corFonteFundo)
sheetDados.write('A2', 'Amanda', corFonte)
sheetDados.write('B2', 21, corFonte)
sheetDados.write('A3', 'Roberto', corFonte)
sheetDados.write('B3', 28, corFonte)

minhaPlanilha.close()

os.startfile(caminhoArquivo)