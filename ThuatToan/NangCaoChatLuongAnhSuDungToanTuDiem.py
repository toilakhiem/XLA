import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_transform(input_image, c):
    output_image = c * np.log1p(input_image)
    return output_image

def power_transform(input_image, c, gamma):
    output_image = c * np.power(input_image, gamma)
    return output_image

def NCCLA_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the input image to np.float32
    input_image_float32 = input_image.astype(np.float32) / 255.0

    # Xử lý bằng biến đổi log
    c1 = 1.0  # Hằng số c cho biến đổi log
    log_transformed_image1 = log_transform(input_image_float32, c1)

    # Xử lý bằng biến đổi mẫu
    c2 = 1.0  # Hằng số c cho biến đổi mẫu
    gamma = 0.67  # Tham số gamma cho biến đổi mẫu
    power_transformed_image = power_transform(log_transformed_image1, c2, gamma)

    # Xử lý bằng biến đổi log lần nữa
    c3 = 1.0  # Hằng số c cho biến đổi log lần nữa
    log_transformed_image2 = log_transform(power_transformed_image, c3)

    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor((log_transformed_image2 * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)), plt.title('Processed Image')
    plt.show()
