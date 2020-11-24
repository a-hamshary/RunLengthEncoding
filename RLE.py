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

    vertical_str = "V "
    vertical_str += str(width)
    vertical_str += " "
    vertical_str += str(height)

    pixel_value = np_img[0]
    print(f"np img: {np_img[0]}")
    print(f"pixel value: {pixel_value}")
    first_element = 0
    last_element = 0

    for i in range(0, width):
        for j in range(0, height):
            if j % width-1 == 0:
                vertical_str += "\n"
            if np_img[j] != pixel_value:
                #vertical_str += "PV"
                vertical_str += str(pixel_value)
                vertical_str += " "
                #vertical_str += "F"
                vertical_str += str(first_element)
                vertical_str += " "
                #vertical_str += "L"
                vertical_str += str(last_element)
                vertical_str += " "

                pixel_value = np_img[j]
                first_element = j
            last_element = j

    # print(horizontal_str)
    return vertical_str


def toStrH(img_obj):
    width, height = img_obj.size
    print(width, height)
    np_img = np.array(img_obj).flatten()

    horizontal_str = "H "
    horizontal_str += str(width)
    horizontal_str += " "
    horizontal_str += str(height)

    pixel_value = np_img[0]
    first_element = 0
    last_element = 0

    for i in range(0, height):
        for j in range(0, width):
            if j % width-1 == 0:
                horizontal_str += "\n"
            if np_img[j] != pixel_value:
                #horizontal_str += "PV"
                horizontal_str += str(pixel_value)
                horizontal_str += " "
                #horizontal_str += "F"
                horizontal_str += str(first_element)
                horizontal_str += " "
                #horizontal_str += "L"
                horizontal_str += str(last_element)
                horizontal_str += " "

                pixel_value = np_img[j]
                first_element = j
            last_element = j

    # print(horizontal_str)
    print(len(horizontal_str))
    return horizontal_str


def toFile(rle_string, filename):
    thisfile = open(filename, "w")
    thisfile.write(rle_string)
    thisfile.close()

    text = open(filename, "r")

    count = 0
    for line in text:
        words = line.split(" ")
        for word in words:
            count += 1
    print(f"count {count}")

    return thisfile


a = imOpen("Bars.bmp")
vs = toStrV(a)
toFile(vs, "Bars_V.txt")

hs = toStrH(a)
toFile(hs,"Bars_H.txt" )