import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def imOpen(input_img):
    im = Image.open(input_img)
    im = im.convert("L")
    return im
    #im.show()
    #plt.imshow(im)
    #plt.show()

def toStrV(img_obj):
    width, height = img_obj.size
    print(width, height)
    np_img = np.array(img_obj).flatten()

    horizontal_str = "V "
    horizontal_str += str(width)
    horizontal_str += " "
    horizontal_str += str(height)
    horizontal_str += "\n"

    pixel_value = np_img[0]
    print(f"np img: {np_img[0]}")
    print(f"pixel value: {pixel_value}")
    first_element = 0
    last_element = 0

    for i in range(0, width):
        for j in range(0, height):
            if j % width-1 == 0:
                horizontal_str += "\n"
            if np_img[j] != pixel_value:
                horizontal_str += "PV"
                horizontal_str += str(pixel_value)
                horizontal_str += " "
                horizontal_str += "F"
                horizontal_str += str(first_element)
                horizontal_str += " "
                horizontal_str += "L"
                horizontal_str += str(last_element)
                horizontal_str += " "

                pixel_value = np_img[j]
                first_element = j
            last_element = j

    # print(horizontal_str)
    return horizontal_str


def toStrH(img_obj):
    width, height = img_obj.size
    print(width, height)
    np_img = np.array(img_obj).flatten()

    horizontal_str = "H "
    horizontal_str += str(width)
    horizontal_str += " "
    horizontal_str += str(height)
    horizontal_str += "\n"

    pixel_value = np_img[0]
    first_element = 0
    last_element = 0

    for i in range(0, height):
        for j in range(0, width):
            if j % width-1 == 0:
                horizontal_str += "\n"
            if np_img[j] != pixel_value:
                horizontal_str += "PV"
                horizontal_str += str(pixel_value)
                horizontal_str += " "
                horizontal_str += "F"
                horizontal_str += str(first_element)
                horizontal_str += " "
                horizontal_str += "L"
                horizontal_str += str(last_element)
                horizontal_str += " "

                pixel_value = np_img[j]
                first_element = j
            last_element = j

    # print(horizontal_str)
    return horizontal_str

def toFile(text, file):
    thisfile = open(file, "w")
    thisfile.write(text)
    thisfile.close()

    return thisfile


a = imOpen("Bars.bmp")
s = toStrV(a)
toFile(s, "Bars_V.txt")

x = toStrH(a)
toFile(x,"Bars_H.txt" )