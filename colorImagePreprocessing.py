import cv2
import numpy as np
import matplotlib.pyplot as plt

def separatingColor(image):
    B, G, R = cv2.split(image)
    zeroes = np.zeros_like(B)

    redImage = cv2.merge([R, zeroes, zeroes])
    greenImage = cv2.merge([zeroes, G, zeroes])
    blueImage = cv2.merge([zeroes, zeroes, B])

    return redImage, greenImage, blueImage

def colorHistogram(image):
    redImage, greenImage, blueImage = separatingColor(image)

    # Create a 3x2 figure
    plt.figure(figsize=(12, 9))

    # Red Channel
    plt.subplot(3, 2, 1)
    plt.imshow(redImage)
    plt.title("Red Channel")
    plt.axis("off")

    plt.subplot(3, 2, 2)
    redHistogram, _ = np.histogram(image[:, :, 2], bins=256, range=[0, 256])
    plt.bar(range(256), redHistogram, color='red', width=1)
    plt.title("Red Pixel Intensity")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    # Green Channel
    plt.subplot(3, 2, 3)
    plt.imshow(greenImage)
    plt.title("Green Channel")
    plt.axis("off")

    plt.subplot(3, 2, 4)
    greenHistogram, _ = np.histogram(image[:, :, 1], bins=256, range=[0, 256])
    plt.bar(range(256), greenHistogram, color='green', width=1)
    plt.title("Green Pixel Intensity")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    # Blue Channel
    plt.subplot(3, 2, 5)
    plt.imshow(blueImage)
    plt.title("Blue Channel")
    plt.axis("off")

    plt.subplot(3, 2, 6)
    blueHistogram, _ = np.histogram(image[:, :, 0], bins=256, range=[0, 256])
    plt.bar(range(256), blueHistogram, color='blue', width=1)
    plt.title("Blue Pixel Intensity")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()
