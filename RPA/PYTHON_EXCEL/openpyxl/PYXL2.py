from openpyxl import load_workbook
import os

nome_arquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\openpyxl\\InserirDados.xlsx'
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

dadosTabela = [
    ['Nome', 'Idade'],
    ['Berenice', 28],
    ['Amanda', 21],
    ['Roberto', 24],
    ['Fernanda', 9],
    ['Gabriel', 14],
]

for linha in dadosTabela:
    sheet_selecionada.append(linha)



planilha_aberta.save(filename=nome_arquivo)

os.startfile(nome_arquivo)
