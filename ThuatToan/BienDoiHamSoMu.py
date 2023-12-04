import cv2
import numpy as np
import matplotlib.pyplot as plt

def BDHSM_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    c = 1.0
    gamma = 2
    power_transformed_image = (c * np.power(input_image, gamma)).astype(np.uint8)

    # Display the original and processed images
    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(power_transformed_image, cv2.COLOR_BGR2RGB)), plt.title('Processed Image')
    plt.show()

