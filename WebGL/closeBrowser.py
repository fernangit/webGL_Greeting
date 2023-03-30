import pyautogui

def closeBrowser():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    pyautogui.keyUp('ctrl')

if __name__ == '__main__':
    closeBrowser()
