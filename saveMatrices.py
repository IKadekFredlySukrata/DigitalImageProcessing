import cv2
import numpy as np

def save_channel_to_file(filename, channel):
    if len(channel.shape) == 3:
        channel = channel[:, :, 0]
    
    np.savetxt(filename, channel, fmt='%3d', delimiter=' ', newline='\n')

def process_image(colorImage, grayImage):
    B, G, R = cv2.split(colorImage)

    save_channel_to_file("1Red_Channel.txt", R)
    save_channel_to_file("2Green_Channel.txt", G)
    save_channel_to_file("3Blue_Channel.txt", B)
    save_channel_to_file("4Grayscale.txt", grayImage)

    print("Files saved successfully.")
