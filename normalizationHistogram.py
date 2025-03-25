import cv2
import numpy as np
import matplotlib.pyplot as plt

def normalizeHistogram(image):
    # Normalizing Histogram using OpenCV
    normalizedImageLibraryCalculation = cv2.normalize(image.astype(np.float32), None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    normalizedImageLibraryCalculation = normalizedImageLibraryCalculation.astype(np.uint8)

    # Manual Normalization: Rescale pixel values to 0-255
    min_val, max_val = image.min(), image.max()
    normalizedImageManualCalculation = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    return image, normalizedImageLibraryCalculation, normalizedImageManualCalculation