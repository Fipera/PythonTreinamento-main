import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)

emailTo = "ana@gmail.com"
nome = "Ana"

mail.To = emailTo
mail.Subject = 'Meu primeiro email PYTHON/OUTLOOK'
mail.HTMLBody = f"""
<p> Boa noite <b>{nome}</b>.</p>
<p><font color="red"><b><u>Aqui está o seu primeiro email enviado com PYTHON/OUTLOOK.</b></u></font></p>
<p> <a href="https://www.google.com/">Clique aqui para acessar o nosso site</a> </p>
<p><img src="C:\\img\\imagem teste.jpg">.</p>
"""

mail.save()