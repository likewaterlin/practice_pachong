# -*- coding: utf-8 -*-
import pytesseract

# pip3 install pytesseract
from PIL import Image

im = Image.open('test.jpg')

data = pytesseract.image_to_string(im)

print(data)
