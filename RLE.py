import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def imOpen(input_img):
    im = Image.open(input_img)
    return im
    #im.show()
    #plt.imshow(im)
    #plt.show()
    #im = im.convert("L")
    #im.show()


def toStrH(img_obj):
    width, height = img_obj.size
    np_img = np.array(img_obj).flatten()
    length = np.size(np_img)

    horizontal_str = "H "
    horizontal_str += str(width)
    horizontal_str += " "
    horizontal_str += str(height)
    horizontal_str += "\n"
    horizontal_str += "PV:"
    horizontal_str += str(np_img[0])
    horizontal_str += " "
    horizontal_str += "F:"
    horizontal_str += str(0)
    horizontal_str += " "

    #print(horizontal_str)
    #print(length)

    for i in range(1, length):
        last_element = i - 1
        current_element = i

        if i % width == 0:
            horizontal_str += "\n"

        if np_img[current_element] == np_img[last_element]:
            last_element = i

        if np_img[current_element] != np_img[last_element]:
            horizontal_str += "L:"
            horizontal_str += str(last_element)
            horizontal_str += " "

            horizontal_str += "PV:"
            horizontal_str += str(np_img[current_element])
            horizontal_str += " "

            horizontal_str += "F:"
            horizontal_str += str(current_element)
            horizontal_str += " "

    print(horizontal_str)


def toStrH2(img_obj):
    width, height = img_obj.size
    np_img = np.array(img_obj)
    print(width, height)

    horizontal_str = "H "
    horizontal_str += str(width)
    horizontal_str += " "
    horizontal_str += str(height)
    horizontal_str += "\n"

    last_element = 0
    first_element = 0
    pixel_value = 0
    for i in range (0, width):
        for  j in range(0, height):
            if img_obj[j] == img_obj[j-1]:
                last_element = j
            if img_obj[j] != img_obj[j-1]:
                horizontal_str += "PV"
                horizontal_str += pixel_value
                horizontal_str += "F"
                horizontal_str += str(first_element)
                horizontal_str += " "
                horizontal_str += "L"
                horizontal_str += str(last_element)

                pixel_value = img_obj[j]
                first_element = j
                last_element = j


def toStrH3(img_obj):
    width, height = img_obj.size
    print(width, height)
    np_img = np.array(img_obj).flatten()

    horizontal_str = "H "
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
            if j % width == 0:
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

                pixel_value = np_img[j]
                first_element = j
            last_element = j

    print(horizontal_str)

def toFile(text, file):
    thisfile = open(file, "w")
    thisfile.write(text)
    thisfile.close()

    return thisfile


a = imOpen("Ocean.bmp")
toStrH3(a)
