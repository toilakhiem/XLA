import cv2
import numpy as np
import matplotlib.pyplot as plt

def BDL_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the input image to np.float32
    input_image_float32 = input_image.astype(np.float32) / 255.0

    # Apply logarithmic transformation
    c = 1
    output_image = c * np.log1p(input_image_float32)

    # Display the original and processed images
    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor((output_image * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)), plt.title('Processed Image')
    plt.show()
