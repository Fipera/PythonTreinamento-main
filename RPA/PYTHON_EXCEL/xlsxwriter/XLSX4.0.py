import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\FormatacaoCondicional.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = workbook.add_worksheet("Dados")

formatoMaior = workbook.add_format({
    'bg_color': 'green',
    'font_color': 'white'
})

formatoMenor = workbook.add_format({
    'bg_color': 'red',
    'font_color': 'white'
})

inserirDados = [
    ["Coluna1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [23, 32, 76, 51],
    [43, 29, 34, 12],
    [29, 58, 73, 19],
]

sheetDados.write("A1", ">= 50 = VERDE /// <= 50 = VERMELHO")

for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)

sheetDados.conditional_format('B4:E7', {
    'type': 'cell',
    'criteria': '>=',
    'value': 50,
    'format': formatoMaior
    })

sheetDados.conditional_format('B4:E7', {
    'type': 'cell',
    'criteria': '<=',
    'value': 50,
    'format': formatoMenor
    })

workbook.close()

os.startfile(caminhoArquivo)