import cv2
import showImages
import lowPassManualCalculation

def normalMean(image):
    print("\nLow Pass: Normal Average")
    blurValue = int(input("\nFrom 1 - 25, please choose how hard the blur would be\n>> "))

    normalAverageBlur = cv2.blur(image, (blurValue, blurValue))
    normalAverageBlurManualCalculation = lowPassManualCalculation.lowPassNormalMean(image, blurValue)

    showImages.threeImages(image, normalAverageBlur, normalAverageBlurManualCalculation)

def gaussianMean(image):
    print("\nLow Pass: Weighted Average (Gaussian)")
    
    while True:
        try:
            blurValue = int(input("\nPlease choose how hard the blur would be (3, 5, 7)\n>> ").strip())
            if blurValue in [3, 5, 7]:  
                break
            else:
                print("Invalid input! Please enter 3, 5, or 7.")
        except ValueError:
            print("Invalid input! Please enter a number (3, 5, or 7).")
    
    gaussionAverageBlur = cv2.GaussianBlur(image, (blurValue, blurValue), 0)
    gaussionAverageBlurManualCalculation = lowPassManualCalculation.lowPassGaussianMean(image, blurValue)

    showImages.threeImages(image, gaussionAverageBlur, gaussionAverageBlurManualCalculation)

def median(image):
    print("\nLow Pass: Median")

    blurValue = int(input("\nPlease Choose the Value (3, 5, 7)\n>> "))

    if blurValue not in [3, 5, 7, 9, 11, 25]:
        print("Please input the supportted value")
        median(image)
    
    medianBlur = cv2.medianBlur(image, blurValue)
    medianBlurManualCalculation = lowPassManualCalculation.lowPassMedian(image, blurValue)

    showImages.threeImages(image, medianBlur, medianBlurManualCalculation)

def bilateral(image):
    print("\nLow Pass: Bilateral")

    blurValue = int(input("\nPlease Choose the Value (3, 5, 7)\n>> "))

    if blurValue not in [3, 5, 7, 9, 11, 25]:
        print("Please input the supportted value")
        bilateral(image)

    bilateralBlur = cv2.bilateralFilter(image, blurValue, 75, 75)
    bilateralBlurManualCalculation = lowPassManualCalculation.lowPassBilateral(image, blurValue, 75, 75)

    showImages.threeImages(image, bilateralBlur, bilateralBlurManualCalculation)
    