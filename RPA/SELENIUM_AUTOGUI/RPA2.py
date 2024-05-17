import pyautogui

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('excel')
    pyautogui.press('enter')
    pyautogui.sleep(5)
    pyautogui.click(x=609, y=260)
    pyautogui.sleep(3)
    pyautogui.typewrite('Escolhemos o excel')

elif opcao == 'Word':
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('winword')
    pyautogui.press('enter')
    pyautogui.sleep(5)
    pyautogui.click(x=609, y=260)
    pyautogui.sleep(3)
    pyautogui.typewrite('Escolhemos o word')

    

elif opcao == 'Notepad':
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.typewrite('Escolhemos o notepad')
