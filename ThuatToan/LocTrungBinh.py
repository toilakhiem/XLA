import cv2
import numpy as np

def average_filter(input_image, kernel_size):
    """
    Thực hiện lọc trung bình trên ảnh đầu vào.

    :param input_image: Ảnh đầu vào (grayscale).
    :param kernel_size: Kích thước của kernel (chẳng hạn (3, 3) cho kernel 3x3).
    :return: Ảnh sau khi áp dụng lọc trung bình.
    """
    height, width = input_image.shape
    output_image = np.zeros((height, width), dtype=np.uint8)

    k_height, k_width = kernel_size
    k_half_height = k_height // 2
    k_half_width = k_width // 2

    for i in range(k_half_height, height - k_half_height):
        for j in range(k_half_width, width - k_half_width):
            # Tính giá trị trung bình của các pixel trong vùng lân cận
            neighborhood = input_image[i - k_half_height:i + k_half_height + 1, j - k_half_width:j + k_half_width + 1]
            output_image[i, j] = np.mean(neighborhood)

    return output_image

# Đọc ảnh đầu vào
input_image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Thiết lập kích thước kernel (ví dụ: 3x3)
kernel_size = (3, 3)

# Áp dụng lọc trung bình
output_image = average_filter(input_image, kernel_size)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', input_image)
cv2.imshow('Average Filtered Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
