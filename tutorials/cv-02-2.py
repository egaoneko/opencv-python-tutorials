import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def showImage(img_flag):
    img_file = '../img/sana01.jpeg'
    window_title = 'sana'

    img = cv2.imread(img_file, img_flag)

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title(window_title)
    plt.show()

showImage(cv2.IMREAD_GRAYSCALE)