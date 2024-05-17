import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\FormatacaoSimbolos.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = workbook.add_worksheet("Dados")



inserirDados = [
    ["Coluna1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [23, 32, 76, 51],
    [43, 29, 34, 12],
    [29, 58, 73, 19],
    [18, 30, 45, 12],
]

sheetDados.write("A1", "Formatacao com icones")

for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)

sheetDados.conditional_format('B4:E4', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights',
    })

sheetDados.conditional_format('B5:E5', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights',
    'reverse_icons': True,
    })

sheetDados.conditional_format('B6:E6', {
    'type': 'icon_set',
    'icon_style': '3_arrows',
    })

sheetDados.conditional_format('B7:E7', {
    'type': 'icon_set',
    'icon_style': '4_arrows',
    })

sheetDados.conditional_format('B8:E8', {
    'type': 'icon_set',
    'icon_style': '5_ratings',
    })


workbook.close()

os.startfile(caminhoArquivo)