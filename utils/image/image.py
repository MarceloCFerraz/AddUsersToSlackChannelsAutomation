

import ctypes
import cv2
import numpy as np
from PIL import ImageGrab


def erode(img):
    return cv2.erode(img, np.ones((2, 2), np.uint8))


def dilate(img):
    return cv2.dilate(img, np.ones((2, 2), np.uint8))


def opening(img):
    erosao = erode(img)
    return cv2.dilate(erosao, np.ones((2, 2), np.uint8))


def closing(img):
    dilatar = dilate(img)
    return cv2.erode(dilatar, np.ones((2, 2), np.uint8))


def expand(img, fator_de_ampliação):
    # cv2.INTER_NEAREST (vizinho mais próximo. mais rápido)
    # cv2.INTER_LINEAR (bilinear. padrão. boa para aumentar ou diminuir)
    # cv2.INTER_AREA (melhor para redução. para ampliar, é semelhante ao nearest)
    # cv2.INTER_CUBIC (2ª melhor para ampliação. matriz 4x4 de pixels vizinhos
    # cv2.INTER_LANCZOS4 (melhor para ampliação. matriz 8x8 pixels vizinhos
    return cv2.resize(img, None, fx=fator_de_ampliação, fy=fator_de_ampliação, interpolation=cv2.INTER_CUBIC)


def invert(img):
    return 255 - img


def printWholeScreen():
    user32 = ctypes.windll.user32
    x = user32.GetSystemMetrics(0)
    y = user32.GetSystemMetrics(1)
    
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return ImageGrab.grab(bbox=(0, 0, x, y))


def printScreen(x1, y1, x2, y2):
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))


def showImage(img, title):
    cv2.imshow(title, img)
    cv2.waitKey()


def imgToRgb(img):
    rgb = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return rgb


def imgToGray(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    return gray


def bgrToGray(bgr):
    gray = cv2.cvtColor(np.array(bgr), cv2.COLOR_BGR2GRAY)
    return gray

