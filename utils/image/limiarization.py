import cv2
from utils.image.image import imgToGray, imgToRgb


def rawOtsu(img):
    img = otsu(imgToGray(imgToRgb(img)))
    return img


def basic(gray):
    limiar, img = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def basicWithInput(gray, limiar):
    limiar, img = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def otsu(gray):
    limiar, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # print("- Limiar Gaussiano: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def mediumAdapt(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def gaussAdapt(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img

