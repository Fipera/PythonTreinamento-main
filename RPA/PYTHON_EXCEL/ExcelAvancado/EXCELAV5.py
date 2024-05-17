from openpyxl import load_workbook
import os

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

nome_arquivo = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\ExcelAvançado_Quebras_Email\\ListaEmail.xlsx'
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):

    nome = sheet_selecionada['A%s' % linha].value
    nomeCompleto = sheet_selecionada['B%s' % linha].value
    email = sheet_selecionada['C%s' % linha].value

    mail = outlook.CreateItem(0)


    mail.To = email
    mail.Subject = 'Lista de vendas ' + nomeCompleto
    mail.HTMLBody = f"""
    <p> Boa noite <b>{nome}</b>.</p>
    <p>Segue o relatório com suas vendas.</p>
    <p>Atenciosamente.</p>
    <p><img src="C:\\img\\imagem teste.jpg">.</p>
    """

    anexoEmail = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\ExcelAvançado_Quebras_Email\\' + nomeCompleto + '.xlsx'
    mail.Attachments.Add(anexoEmail)
    mail.save()