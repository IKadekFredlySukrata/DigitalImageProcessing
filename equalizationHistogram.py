import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalizeHistogram(image):
    # Equalizing Histogram using CV2 Python Library
    equalizedImageLibraryCalculation = cv2.equalizeHist(image)
    # Equalizing Histogram using Manual Calculation
    histogram, _ = np.histogram(image.flatten(), bins=256, range=[0,255])
    
    cumulativeFrequency = histogram.cumsum()
    cumulativeFrequencyNormalized = cumulativeFrequency / cumulativeFrequency[-1]
    
    cumulativeFrequencyRounded = np.round(cumulativeFrequencyNormalized * 255).astype(np.uint8)
    
    equalizedImageManualCalculation = cumulativeFrequencyRounded[image]
    
    return image, equalizedImageLibraryCalculation, equalizedImageManualCalculation