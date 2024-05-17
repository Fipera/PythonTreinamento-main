from openpyxl import load_workbook
import os

nome_arquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\openpyxl\\DeletarLinhaColuna.xlsx'
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)

sheet_selecionada.delete_cols(2)



planilha_aberta.save(filename=nome_arquivo)

os.startfile(nome_arquivo)
