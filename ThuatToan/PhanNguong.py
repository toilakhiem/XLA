import cv2
import numpy as np
from matplotlib import pyplot as plt

def PN_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    ret, thresh1 = cv2.threshold(input_image,127,255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(input_image,127,255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(input_image,127,255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(input_image,127,255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(input_image,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [input_image, thresh1, thresh2, thresh3, thresh4,thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()