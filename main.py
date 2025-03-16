import cv2
import findImage
import grayImagePreprocessing
import colorImagePreprocessing
import saveMatrices
import equalizationHistogram


# Import File
image = findImage.findImage()

# Area of Interest (ROI) Box
roiBox = cv2.selectROI("Select ROI and Press ENTER", image)
cv2.destroyWindow("Select ROI and Press ENTER")
x, y, w, h = map(int, roiBox)

roiColor = image[y:y + h, x:x + w]
roiGray = cv2.cvtColor(roiColor, cv2.COLOR_BGR2GRAY)

showPreprocessingResult = input("Do you wanna see the pre-processing result?\nYes / No \n>> ").strip().lower()
if showPreprocessingResult not in ["no", "n", "nah"]:
    grayImagePreprocessing.grayHistogram(roiGray, x, y, w, h)
    colorImagePreprocessing.colorHistogram(roiColor)
    saveMatrices.process_image(roiColor, roiColor)

while True:
    print("List of Program")
    print("1. Histogram Equalization")
    print("2. Histogram Normalization")
    # Add a New Technique
    print("Exit")
    
    choice = input("Want do you to do?\n>> ").strip().lower()

    if choice == "exit":
        break
    
    try:
        choice = int(choice)
    except ValueError:
        print("Please re-input your choice...")
        continue

    match choice:
        case 1:
            print("Calculating...\nAnd these are the results")
            equalizationHistogram.equalizeHistogram(roiGray)
            # This equalization done in order to get more information out
            # from an image, cause sometimes the detail is hiding in between
            # the contrast...

        case 2:
            print("Calculating...\nAnd these are the results")


        case _:
            print("Hmm... Please, try again")

    again = input("\nWanna try another program?\nYes / No\n>> ").strip().lower()
    if again not in ["yes", "y"]:
        print("Good luck out there, I'm proud of you... See ya...")
        break