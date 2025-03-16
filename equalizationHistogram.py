import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalizeHistogram(image):
    # Equalizing Histogram using CV2 Python Library
    result = cv2.equalizeHist(image)

    # Making the Histogram for Both Before and After
    beforeHistogram, _ = np.histogram(image.flatten(), bins=256, range=[0, 255])
    afterHistogram, _ = np.histogram(result.flatten(), bins=256, range=[0, 255])

    # Plotting All the Data
    plt.figure(figsize=(12, 9))

    plt.subplot(3, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Before Equalization")
    plt.axis("off")

    plt.subplot(3, 2, 2)
    plt.bar(range(256), beforeHistogram, color='black', width=1)
    plt.title("Pixel Frequency Distribution")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    
    plt.subplot(3, 2, 3)
    plt.imshow(result, cmap='gray')
    plt.title("After Equalization")
    plt.axis("off")

    plt.subplot(3, 2, 4)
    plt.bar(range(256), afterHistogram, color='black', width=1)
    plt.title("Pixel Frequency Distribution")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()
