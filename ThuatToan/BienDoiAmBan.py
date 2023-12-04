import cv2
import numpy as np
import matplotlib.pyplot as plt

def BDAB_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    output_image = cv2.bitwise_not(input_image)

    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)), plt.title('Processed Image')
    plt.show()

