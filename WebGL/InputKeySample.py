#バックグラウンドで実行する
#pip install pyautogui
#https://magazine.techacademy.jp/magazine/46562
import time
import pyautogui
import startBrowser

startBrowser.startBrowser('http://localhost:8000/')
time.sleep(30)
print('最大化')
#pyautogui.typewrite('x')
pyautogui.hotkey('x')
pyautogui.click(500,500)
pyautogui.hotkey('f2')
#pyautogui.click(500,500)

#pip install keyboard
#https://www.delftstack.com/ja/howto/python/python-simulate-keyboard-input/
#import time
#import keyboard
#time.sleep(10)
#keyboard.press_and_release('x')

