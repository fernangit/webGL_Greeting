import time
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
#import keyboard
import pyautogui
#import winsound
#import pygame
from playsound import playsound

import startServer
import startBrowser

#pygame.mixer.init(frequency = 44100)    # 初期設定
#def playSound(soundfile):
#    pygame.mixer.music.load(soundfile)     # 音楽ファイルの読み込み
#    pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
def setMotion(sec, key):
    print(sec, key)
    time.sleep(sec)
    pyautogui.hotkey(key)

def changeMotion():
    #フルスクリーン
#    keyboard.press_and_release('x')
    pyautogui.hotkey('x')
    pyautogui.click(500,500)
    time.sleep(1)
    while(True):
        #モーション変更
        print('change motion')
#        keyboard.press_and_release('f2')
#        pyautogui.hotkey('f2')
        thread = threading.Thread(target=setMotion, args=(1.5,'f2'))
        thread.start()
#        winsound.PlaySound("アカリがやってきたぞっ.wav", winsound.SND_FILENAME)
        playsound('アカリがやってきたぞっ.wav')
#        playSound('アカリがやってきたぞっ.wav')
        time.sleep(1)
#        keyboard.press_and_release('2')
        pyautogui.hotkey('2')
        time.sleep(1)

# with ThreadPoolExecutor() as executor:
# #with ProcessPoolExecutor() as executor:
# #    executor.submit(changeMotion)
# #    executor.submit(startServer.startServer, 8000)
# #    time.sleep(5)
#     executor.submit(startBrowser.startBrowser, "http://localhost:8000/")

# #ブラウザ起動　画面MAX
startBrowser.startBrowser('http://localhost:8000/')
#Unityが立ち上がるまで待つ
time.sleep(30)
# #モーション起動
print('モーション起動')
changeMotion()

# #ブラウザ起動　画面MAX
# print('start browser')
# subprocess.run('python startBrowser.py')
# #thread = threading.Thread(target=startBrowser.startBrowser("http://localhost:8000/"))
# #thread.start()

# #モーション起動
# print('start motion')
# thread = threading.Thread(target=changeMotion())
# thread.start()

# #サーバー起動
# print('start server')
# subprocess.run('python startServer.py')
# #thread = threading.Thread(target=startServer.startServer(8000))
# #thread.start()

