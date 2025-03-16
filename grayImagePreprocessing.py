import matplotlib.pyplot as plt
import numpy as np
def grayHistogram(imageROI, X, Y, W, H):
    histogram, bins = np.histogram(imageROI.flatten(), bins=256, range=[0, 255])
    # Making a New Canvas
    plt.figure(figsize=(12, 5))
    
    # Choosing Position of Subplot 
    plt.subplot(1, 2, 1)

    # Plot ROI Settings
    plt.imshow(imageROI, cmap="gray")
    plt.title(f"Selected ROI (Gray) = {W} x {H}\nStarting Point at ({X}, {Y})")
    plt.colorbar()
    
    # Bar Plot Settings
    plt.subplot(1, 2, 2)
    plt.bar(range(256), histogram, color='black', width=1)
    plt.title("Pixel Intensity Distribution")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()