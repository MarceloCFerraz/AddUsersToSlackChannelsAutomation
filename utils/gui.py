import pyautogui as gui
import time
from utils import common

STANDARD_INTERVAL = 0.1
STANDARD_DURATION = STANDARD_INTERVAL


def ultraFastClick(x, y):
    gui.click(x, y)


def updatePage():
    gui.hotkey("ctrl", "shift", "r")


def click(x, y):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=STANDARD_DURATION*5)


def clickSleep(x, y, sleep):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, interval=STANDARD_INTERVAL*5, duration=STANDARD_DURATION*5)
    time.sleep(sleep)


def rightClickSleep(x, y, sleep):
    gui.rightClick(x, y, STANDARD_INTERVAL, STANDARD_DURATION*10)
    time.sleep(sleep)


def pressKey(key):
    gui.press(key)


def pressKeySleep(key, sleep):
    gui.press(key)
    time.sleep(sleep)


def hotKey(key_1, key_2):
    gui.hotkey(key_1, key_2)
    time.sleep(common.STANDARD_SLEEP_TIME)


def typeSleep(text, seconds):
    gui.typewrite(text, interval=STANDARD_INTERVAL/2)
    time.sleep(seconds)


def countdown(seconds):
    while seconds > 0:
        # if seconds <= 10:
        #     # emite som de alerta com contagem regressiva de 10 segundos
        #     winsound.Beep(900, 100)
        print(seconds)
        seconds -= 1
        time.sleep(1)


def printlessCountdown(seconds):
    time.sleep(seconds)

