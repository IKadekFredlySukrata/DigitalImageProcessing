import tkinter
import tkinter.filedialog
from cv2 import imread

def findImage():
    root = tkinter.Tk()
    root.withdraw()

    imagePath = tkinter.filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif")]
    )

    if not imagePath:
        print("Please Choose One, Dumbass")
        return findImage()

    image = imread(imagePath)
    if image is None:
        print("Failed to Load The Image, Please Try Again...")
        exit()

    return image
