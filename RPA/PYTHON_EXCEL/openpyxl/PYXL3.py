from openpyxl import load_workbook
import os

from openpyxl.styles import Color, PatternFill, Font, Border, Side
from openpyxl.styles import colors
from openpyxl.cell import Cell

nome_arquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\openpyxl\\InserirDadosPintarCelulas.xlsx'
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

corTitulo = PatternFill(start_color='00FFFF00',
    end_color = '00FFFF00',
    fill_type ='solid'
)

corCelulas = PatternFill(start_color='00CCFFCC',
    end_color = '00CCFFCC',
    fill_type ='solid'
)

sheet_selecionada['A1'].fill = corTitulo
sheet_selecionada['B1'].fill = corTitulo

for linha in range(2, len(sheet_selecionada['A']) + 1):

    celulaColunaA = "A" + str(linha)
    celulaColunaB = "B" + str(linha)

    sheet_selecionada[celulaColunaA].fill = corCelulas
    sheet_selecionada[celulaColunaB].fill = corCelulas



planilha_aberta.save(filename=nome_arquivo)

os.startfile(nome_arquivo)