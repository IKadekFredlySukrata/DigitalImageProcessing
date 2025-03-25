import numpy as np

def lowPassNormalMean(image, windowSize):
    # Window Size Calculation
    windowSize = (windowSize - 1) // 2

    # Adding Proper Padding to Match Window Size
    image = np.pad(image, pad_width=windowSize, mode='constant', constant_values=0)
    height, width = image.shape

    # Making a new image template
    result = np.zeros((height - 2 * windowSize, width - 2 * windowSize))

    for i in range(windowSize, height - windowSize):
        for j in range(windowSize, width - windowSize):
            window = image[i - windowSize : i + windowSize + 1, j - windowSize : j + windowSize + 1]
            pixelResult = np.mean(window)

            # Correct indexing for result image
            result[i - windowSize, j - windowSize] = pixelResult

    return result

import numpy as np

def lowPassGaussianMean(image, windowSize):
    # Calculate Half Window Size
    halfWindowSize = (windowSize - 1) // 2

    # Add Proper Padding
    image = np.pad(image, pad_width=halfWindowSize, mode='constant', constant_values=0)
    height, width = image.shape

    # Create Empty Result Image
    result = np.zeros((height - 2 * halfWindowSize, width - 2 * halfWindowSize))

    # Define Gaussian Kernels
    gaussian_kernels = {
        1: np.array([[1, 2, 1], 
                     [2, 4, 2], 
                     [1, 2, 1]]),  # 3x3
        2: np.array([[1,  4,  7,  4,  1], 
                     [4, 16, 26, 16,  4], 
                     [7, 26, 41, 26,  7], 
                     [4, 16, 26, 16,  4], 
                     [1,  4,  7,  4,  1]]),  # 5x5
        3: np.array([[1,   6,  15,  20,  15,  6,  1], 
                     [6,  34,  74,  96,  74, 34,  6], 
                     [15, 74, 144, 178, 144, 74, 15], 
                     [20, 96, 178, 225, 178, 96, 20], 
                     [15, 74, 144, 178, 144, 74, 15], 
                     [6,  34,  74,  96,  74, 34,  6], 
                     [1,   6,  15,  20,  15,  6,  1]])  # 7x7
    }

    # Select the Correct Gaussian Kernel
    kernel = gaussian_kernels[halfWindowSize]
    kernel = kernel / np.sum(kernel)  # Normalize Kernel

    # Apply Convolution
    for i in range(halfWindowSize, height - halfWindowSize):
        for j in range(halfWindowSize, width - halfWindowSize):
            window = image[i - halfWindowSize : i + halfWindowSize + 1, 
                           j - halfWindowSize : j + halfWindowSize + 1]
            
            pixelResult = np.sum(window * kernel)  # Convolution

            result[i - halfWindowSize, j - halfWindowSize] = pixelResult

    return result

def lowPassMedian(image, windowSize):
    halfWindowSize = (windowSize - 1) // 2
    
    image = np.pad(image, pad_width=halfWindowSize, mode='constant', constant_values=0)
    height, width = image.shape
    
    result = np.zeros((height - 2 * halfWindowSize, width - 2 * halfWindowSize))
    
    for i in range(halfWindowSize, height - halfWindowSize):
        for j in range(halfWindowSize, width - halfWindowSize):
            window = image[i - halfWindowSize : i + halfWindowSize + 1,
                           j - halfWindowSize : j + halfWindowSize + 1]
            
            result[i - halfWindowSize, j - halfWindowSize] = np.median(window)

            
    return result

def lowPassBilateral(image, windowSize, sigmaSpatial, sigmaIntensity):
    halfWindowSize = (windowSize - 1) // 2
    image = image.astype(np.float32)
    image = np.pad(image, pad_width=halfWindowSize, mode='reflect')

    height, width = image.shape
    result = np.zeros((height - 2 * halfWindowSize, width - 2 * halfWindowSize), dtype=np.float32)

    x, y = np.mgrid[-halfWindowSize: halfWindowSize + 1, -halfWindowSize: halfWindowSize + 1]
    spatialGaussian = np.exp(-(x**2 + y**2) / (2 * sigmaSpatial**2))

    for i in range(halfWindowSize, height - halfWindowSize):
        for j in range(halfWindowSize, width - halfWindowSize):
            window = image[i - halfWindowSize: i + halfWindowSize + 1, j - halfWindowSize: j + halfWindowSize + 1]

            intensityDiff = window - image[i, j]
            intensityGaussian = np.exp(-(intensityDiff**2) / (2 * sigmaIntensity**2))

            bilateralWeights = spatialGaussian * intensityGaussian
            bilateralWeights /= np.sum(bilateralWeights)
            
            result[i - halfWindowSize, j - halfWindowSize] = np.sum(window * bilateralWeights)

    return result.astype(np.uint8)