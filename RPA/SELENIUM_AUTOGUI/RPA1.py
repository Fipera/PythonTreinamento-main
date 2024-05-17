import pyautogui as autogui

autogui.hotkey('win', 'r')

autogui.sleep(2)

autogui.typewrite('notepad')

autogui.sleep(2)

autogui.press('enter')

autogui.sleep(2)

autogui.typewrite('é o brabo')

autogui.sleep(2)

fecharNotepad = autogui.getActiveWindow()

fecharNotepad.close()

autogui.press('tab')

autogui.sleep(2)

autogui.press('enter')


