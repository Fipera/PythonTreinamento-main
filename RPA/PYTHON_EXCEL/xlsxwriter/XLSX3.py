import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\MergeCells.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")

add_merge_celulas = minhaPlanilha.add_format({
    'bold': True,
    'border' : 6,
    'align' : 'center',
    'valign' : 'vcenter',
    'size' : 30,
    'fg_color' : 'purple',
    'font_color' : 'white'
})

sheetDados.merge_range('B3:I5', 'Merge Células', add_merge_celulas)

minhaPlanilha.close()

os.startfile(caminhoArquivo)