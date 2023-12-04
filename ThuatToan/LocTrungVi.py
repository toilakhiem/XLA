import cv2
import numpy as np
import matplotlib.pyplot as plt

def LTV_process_image(file):
    content = file.read()
    nparr = np.frombuffer(content, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Áp dụng average blur
    blur_average = cv2.blur(input_image, (3, 3))

    # Áp dụng median blur
    kernel_size_median = 3
    blur_median = cv2.medianBlur(input_image, kernel_size_median)

    # Hiển thị hình ảnh gốc và hình ảnh đã xử lý
    plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title('Ảnh gốc')
    plt.subplot(1, 3, 2), plt.imshow(cv2.cvtColor(blur_average, cv2.COLOR_BGR2RGB)), plt.title('Blur Average')
    plt.subplot(1, 3, 3), plt.imshow(cv2.cvtColor(blur_median, cv2.COLOR_BGR2RGB)), plt.title('Blur Median')

    # Chuyển đổi hình ảnh từ BGR sang RGB trước khi hiển thị
    plt.show()

