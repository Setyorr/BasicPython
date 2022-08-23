import pyautogui
def CopyText(nextline=0):
    pyautogui.moveTo(x=1321, y=300 + nextline, duration=1)
    pyautogui.click(x=1321, y=300 + nextline, duration=1)
    pyautogui.dragTo(x=1478, y=300 + nextline, duration=1)
    pyautogui.hotkey('Ctrl','c')
    pyautogui.moveTo(x=696, y=300 + nextline, duration=1)
    pyautogui.click(x=696, y=300 + nextline, duration=1)
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('Enter')
for i in range(3):
    CopyText(50*i)
    
