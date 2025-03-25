import matplotlib.pyplot as plt
import numpy as np

def twoImages(imageOne, imageTwo):
    img_height, img_width = imageOne.shape[:2]
    
    scale_factor = 8 / max(img_height, img_width)
    fig_width = img_width * scale_factor
    fig_height = img_height * scale_factor

    plt.figure(figsize=(fig_width, fig_height))

    plt.subplot(1, 2, 1)
    plt.imshow(imageOne, cmap='gray')
    plt.title("Before")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imageTwo, cmap='gray')
    plt.title("After")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
    
def threeImages(imageOne, imageTwo, imageThree):
    img_height, img_width = imageOne.shape[:2]
    
    scale_factor = 8 / max(img_height, img_width)
    fig_width = img_width * scale_factor
    fig_height = img_height * scale_factor

    plt.figure(figsize=(fig_width, fig_height))

    plt.subplot(1, 3, 1)
    plt.imshow(imageOne, cmap='gray')
    plt.title("Before")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(imageTwo, cmap='gray')
    plt.title("Library Calculation")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.imshow(imageThree, cmap='gray')
    plt.title("Manual Calculation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

def threeImagesWithHistogram(imageOne, imageTwo, imageThree):
    img_height, img_width = imageOne.shape[:2]
    
    scale_factor = 8 / max(img_height, img_width)
    fig_width = img_width * scale_factor
    fig_height = img_height * scale_factor
    
    plt.figure(figsize=(fig_width, fig_height))
    
    # Image Before
    plt.subplot(3, 2, 1)
    plt.imshow(imageOne, cmap='gray')
    plt.title("Before Image")
    plt.axis("off")
    
    # Histogram Before
    histogramOne, binsOne = np.histogram(imageOne, bins=256, range=(0, 255))
    plt.subplot(3, 2, 2)
    plt.bar(binsOne[:-1], histogramOne, color='black')
    plt.title("Before Histogram")
    
    # Image After (Library Calculation)
    plt.subplot(3, 2, 3)
    plt.imshow(imageTwo, cmap='gray')
    plt.title("After (Library Calculation)")
    plt.axis("off")
    
    # Histogram After (Library Calculation)
    histogramTwo, binsTwo = np.histogram(imageTwo, bins=256, range=(0, 255))
    plt.subplot(3, 2, 4)
    plt.bar(binsTwo[:-1], histogramTwo, color='black')
    plt.title("After (Library Calculation)")
    
    # Image After (Manual Calculation)
    plt.subplot(3, 2, 5)
    plt.imshow(imageThree, cmap='gray')
    plt.title("After (Manual Calculation)")
    plt.axis("off")
    
    # Histogram After (Manual Calculation)
    histogramThree, binsThree = np.histogram(imageThree, bins=256, range=(0, 255))
    plt.subplot(3, 2, 6)
    plt.bar(binsThree[:-1], histogramThree, color='black')
    plt.title("After Histogram (Manual Calculation)")
    
    plt.tight_layout()
    plt.show()
