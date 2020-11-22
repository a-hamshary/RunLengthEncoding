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
        if i % width == 0:
            horizontal_str += "\n"

        last_element = i-1
        current_element = i

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


a = imOpen("Ocean.bmp")
toStrH(a)
