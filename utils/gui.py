import pyautogui as gui
import time


def updatePage():
    gui.hotkey("ctrl", "shift", "r")


def click(x, y):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)


def clickSleep(x, y, sleep):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)
    time.sleep(sleep)


def pressKey(tecla):
    gui.press(tecla)


def pressKeySleep(tecla, sleep):
    gui.press(tecla)
    time.sleep(sleep)


def hotKey(key_1, key_2):
    gui.hotkey(key_1, key_2)
    time.sleep(1)


def typeSleep(channel_name, seconds):
    gui.typewrite(channel_name, 0.1)
    time.sleep(seconds)


def countdown(tempo):
    while tempo > 0:
        # if tempo <= 10:
        #     # emite som de alerta com contagem regressiva de 10 segundos
        #     winsound.Beep(900, 100)
        print("{}".format(tempo), end="  ")
        tempo -= 1
        time.sleep(1)


def printlessCountdown(tempo):
    print("Waiting {}s".format(tempo))
    time.sleep(tempo)

