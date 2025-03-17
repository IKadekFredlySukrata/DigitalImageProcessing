import matplotlib.pyplot as plt

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