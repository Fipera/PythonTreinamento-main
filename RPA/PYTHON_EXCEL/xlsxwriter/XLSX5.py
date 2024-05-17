import xlsxwriter as opcoesDoXlsxWriter
import os

caminhoArquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\xlsxwriter\\Grafico.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(caminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Resumo")

negrito = planilhaExcel.add_format({
    'bold': True,
})

titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ["Ana", "Pedro", "Allan", "Francisco", "Rosa", "Amanda"],
    [400, 300, 89, 34, 350, 120],
]

sheetDados.write_row('A1', titulos, negrito)
sheetDados.write_column('A2', dadosTabela[0])
sheetDados.write_column('B2', dadosTabela[1])

graficoColunas = planilhaExcel.add_chart({
    'type': 'column',
})

graficoColunas.add_series({
    'name' : '=Resumo!$B$1',
    'categories' : '=Resumo!$A$2:$A$7',
    'values' : '=Resumo!$B$2:$B$7',
})

graficoColunas.set_title({'name' : 'Grafico total de vendas'})
graficoColunas.set_x_axis({'name' : 'Vendedores'})
graficoColunas.set_y_axis({'name' : 'Vendas'})

graficoColunas.set_style(11)

sheetDados.insert_chart('D2', graficoColunas, {'x_offset': 25, 'y_offset': 10})

############# GRAFICO 2 ################

graficoEmpilhado = planilhaExcel.add_chart({
    'type': 'area',
    'subtype': 'stacked',
})

graficoEmpilhado.add_series({
    'name' : '=Resumo!$B$1',
    'categories' : '=Resumo!$A$2:$A$7',
    'values' : '=Resumo!$B$2:$B$7',
})

graficoEmpilhado.set_title({'name' : 'Grafico total de vendas'})
graficoEmpilhado.set_x_axis({'name' : 'Vendedores'})
graficoEmpilhado.set_y_axis({'name' : 'Vendas'})

graficoEmpilhado.set_style(11)

sheetDados.insert_chart('L2', graficoEmpilhado, {'x_offset': 25, 'y_offset': 10})




planilhaExcel.close()

os.startfile(caminhoArquivo)