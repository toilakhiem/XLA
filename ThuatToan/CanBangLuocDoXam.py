import cv2
import numpy as np
import matplotlib.pyplot as plt

def hist_equalize(img):
    # 1. calclate hist
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # 2. normalize hist
    h, w = img.shape[:2]
    hist = hist/(h*w)

    # 3. calculate CDF
    cdf = np.cumsum(hist)
    s_k = (255 * cdf - 0.5).astype("uint8")
    return s_k

def CBLDX_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    s_k = hist_equalize(input_image)
    equalized_img = cv2.LUT(input_image, s_k)

    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(equalized_img, cv2.COLOR_BGR2RGB)), plt.title('Equalized Image')
    plt.show()
