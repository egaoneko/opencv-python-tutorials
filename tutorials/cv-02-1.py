import cv2 #OpenCV 패키지 import
import numpy as np

def showImage(img_flag):
    img_file = '../img/sana01.jpeg'
    window_title = 'sana'

    img = cv2.imread(img_file, img_flag)

    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
    cv2.imshow(window_title, img)

    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        cv2.destoryAllWindows()
    elif key == ord('c'):
        cv2.imwrite('../img/sana_copy.jpg', img)
        cv2.destoryAllWindows()

# showImage(cv2.IMREAD_COLOR)
showImage(cv2.IMREAD_GRAYSCALE)
# showImage(cv2.IMREAD_UNCHANGED)