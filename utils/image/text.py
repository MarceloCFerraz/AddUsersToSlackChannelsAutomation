from utils.image import image
from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract as tesseract

tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extractText(capture):
    # Receives a BGR image and converts it to monochrome 
    # to extract it's text more easily
    texto = tesseract.image_to_string(
        cv2.cvtColor(np.array(capture), cv2.COLOR_BGR2GRAY), 
        lang='por+eng'
    )
    texto = texto.split('\n')

    textofinal = ""

    for linha in texto:
        if not linha.isspace() and len(linha) > 0:
            textofinal += linha

    return (textofinal)


def extractTextBgr(capture):
    # Receives a gray monochrome image
    texto = tesseract.image_to_string(capture, lang='por+eng')
    texto = texto.split('\n')

    textofinal = ""

    for linha in texto:
        if not linha.isspace() and len(linha) > 0:
            textofinal += linha

    return (textofinal)


def findTextOnImg(dict, img, search):
    achou = False

    print("Searching for {}".format(search))
    x = None
    y = None
    w = None
    h = None

    for i in range(0, len(dict["text"])):
        reliability = int(float(dict["conf"][i]))
        text = dict["text"][i]

        if reliability > 20 and len(text) > 1:
            if search.upper() == text.upper():
                x = dict["left"][i]
                y = dict["top"][i]
                w = dict["width"][i]
                h = dict["height"][i]
                achou = True
                img = cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0,0,0),
                    2,
                )
                print("{}***\n".format(text)+
                      "x: {}\ny: {}\nw: {}\nh: {}".format(x, y, w, h))
            else:
                achou = False                
                # print(text)


    # image.showImage(img)
    return x, y, w, h, img, achou


def extractDict(rgb):
    dict = tesseract.image_to_data(rgb, output_type=tesseract.Output.DICT)
    return dict
