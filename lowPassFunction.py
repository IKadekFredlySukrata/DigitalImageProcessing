import cv2
import matplotlib.pyplot as plt
import showImages

def normalMean(image):
    print("\nLow Pass: Normal Average")
    blurValue = int(input("\nFrom 1 - 25, please choose how hard the blur would be\n>> "))

    normalAverageBlur = cv2.blur(image, (blurValue, blurValue))

    showImages.twoImages(image, normalAverageBlur)

def gaussianMean(image):
    print("\nLow Pass: Weighted Average (Gaussian)")
    
    blurValue = int(input("\nFrom 1 - 25, please choose how hard the blur would be (odd numbers only)\n>> "))

    if blurValue % 2 == 0:
        blurValue += 1

    gaussionAverageBlur = cv2.GaussianBlur(image, (blurValue, blurValue), 0)

    showImages.twoImages(image, gaussionAverageBlur)

def median(image):
    print("\nLow Pass: Median")

    blurValue = int(input("\nPlease Choose the Value (1, 9, 25)\n>> "))

    if blurValue not in [1, 9, 25]:
        print("Please input the supportted value")
        median(image)
    
    medianBlur = cv2.medianBlur(image, blurValue)

    showImages.twoImages(image, medianBlur)

def bilateral(image):
    print("\nLow Pass: Bilateral")

    blurValue = int(input("\nPlease Choose the Value (1, 9, 25)\n>> "))

    if blurValue not in [1, 9, 25]:
        print("Please input the supportted value")
        bilateral(image)

    bilateralBlur = cv2.bilateralFilter(image, blurValue, 75, 75)

    showImages.twoImages(image, bilateralBlur)
    