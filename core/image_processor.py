#!/usr/bin/env python 
# coding:utf-8
import pytesseract
import urllib
import cv2
import numpy as np
from PIL import Image
from uuid import uuid4


def get_image(url=None, path=None):
    if url is not None:
        return url_to_image(url)
    elif path is not None:
        return cv2.imread(path)
    else:
        return None


def process_image(url=None, path=None, lang=None):
    image = get_image(url, path)
    if image is None:
        return "no input image"
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    dst = cv2.fastNlMeansDenoising(th2, 10, 10, 7)
    img_path = "./uploads/%s.jpg" % uuid4()
    cv2.imwrite(img_path, dst)
    cao = Image.open(img_path)
    print("Recognizing...")
    rec_string = pytesseract.image_to_string(cao, lang)
    print("the result is {}".format(rec_string))
    return rec_string


def url_to_image(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
