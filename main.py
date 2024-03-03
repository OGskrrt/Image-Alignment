import cv2
import numpy as np

def restoration(path):
    image = cv2.imread(path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    max_width = 800
    max_height = 600

    height, width, _ = image.shape

    
    # Resize image to fit maximum dimensions
    if width > max_width or height > max_height:
        # Calculate ratio
        ratio = min(max_width / width, max_height / height)

        # resize 
        resized_image = cv2.resize(image, (int(width * ratio), int(height * ratio)))
    else:
        resized_image = image

    cv2.imshow('Original image', resized_image)

    blue_channel = resized_image[:, :, 0]
    cv2.imshow('Blue Channel', blue_channel)

    green_channel = resized_image[:, :, 1]
    cv2.imshow('Green Channel', green_channel)

    red_channel = resized_image[:, :, 2]
    cv2.imshow('Red Channel', red_channel)

    aligned_green_channel = np.zeros_like(green_channel)
    aligned_green_channel[:, :] = green_channel[:, :]

    aligned_red_channel = np.zeros_like(red_channel)
    aligned_red_channel[:, :] = red_channel[:, :]

    aligned_image = np.stack([blue_channel, aligned_green_channel, aligned_red_channel], axis=2)

    cv2.imshow('Aligned first', aligned_image)

    avg_b = np.mean(blue_channel)
    avg_g = np.mean(green_channel)
    avg_r = np.mean(red_channel)

    # Alignment with avarage 
    B_aligned = blue_channel * (avg_g / avg_b)
    G_aligned = green_channel * (avg_g / avg_g)
    R_aligned = red_channel * (avg_g / avg_r)


    aligned_image = cv2.merge([B_aligned.astype(np.uint8), G_aligned.astype(np.uint8), R_aligned.astype(np.uint8)])


    cv2.imshow('Aligned second', aligned_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = r"Alim-Khan-orginal.jpg"
restoration(path)

path = r"Lady.png"
restoration(path)

path = r"gate.jpg"
restoration(path)

path = r"building.jpg"
restoration(path)

