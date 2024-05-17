#CALCULO DE VENDAS POR PESSOA


from openpyxl import load_workbook
from openpyxl import Workbook
import os


arquivoDadosSistema = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\openpyxl\\DadosSistema.xlsx'
planilhaDadosSistema = load_workbook(filename=arquivoDadosSistema)

sheetPlanilhaDadosSistema = planilhaDadosSistema['Dados']

NovoArquivoExcel = Workbook()
nova_planilha = NovoArquivoExcel.active

for linha in range(1, len(sheetPlanilhaDadosSistema['A']) + 1):
    for coluna in range(1, 10):
        nova_planilha.cell(row=linha, column=coluna).value = sheetPlanilhaDadosSistema.cell(row=linha, column=coluna).value

nova_planilha.delete_rows(2)

nova_planilha.delete_cols(2)
nova_planilha.delete_cols(2)

nova_planilha.title = "Dados Funcionarios"
NovoArquivoExcel.create_sheet('Resumo')


selecionaSheetResumoNovaPlanilha = NovoArquivoExcel['Resumo']

selecionaSheetResumoNovaPlanilha['A1'] = "Vendedor"
selecionaSheetResumoNovaPlanilha['B1'] = "Total Vendas"

selecionaSheetResumoNovaPlanilha['A2'] = "Amanda Martins"
selecionaSheetResumoNovaPlanilha['B2'] = "=SUMIF('Dados Funcionarios'!A:C,A2,'Dados Funcionarios'!C:C)"

selecionaSheetResumoNovaPlanilha['A3'] = "Eliane Moreira"
selecionaSheetResumoNovaPlanilha['B3'] = "=SUMIF('Dados Funcionarios'!A:C,A3,'Dados Funcionarios'!C:C)"

selecionaSheetResumoNovaPlanilha['A4'] = "Leonardo Almeida"
selecionaSheetResumoNovaPlanilha['B4'] = "=SUMIF('Dados Funcionarios'!A:C,A4,'Dados Funcionarios'!C:C)"

selecionaSheetResumoNovaPlanilha['A5'] = "Nicolas Pereira"
selecionaSheetResumoNovaPlanilha['B5'] = "=SUMIF('Dados Funcionarios'!A:C,A5,'Dados Funcionarios'!C:C)"


arquivoNovaPlanilha = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\openpyxl\\RelatorioSistema.xlsx'

NovoArquivoExcel.save(filename=arquivoNovaPlanilha)

os.startfile(arquivoNovaPlanilha)
