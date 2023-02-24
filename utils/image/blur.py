
import cv2


def median(img):
    return cv2.medianBlur(img, 3)


def bilateral(img):
    return cv2.bilateralFilter(img, 15, 55, 45)

