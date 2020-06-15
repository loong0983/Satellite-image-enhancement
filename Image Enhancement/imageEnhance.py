"""
imageEnhance.py

YOUR WORKING FUNCTION

"""
import numpy as np
import cv2
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

input_dir = 'input/input'
output_dir = 'output/output'

# you are allowed to import other Python packages above
##########################
def enhanceImage(img):
    # Inputs
    # inputImg: Input image, a 3D numpy array of row*col*3 in BGR format
    #
    # Output
    # outputImg: Enhanced image
    #
    #########################################################################
    # ADD YOUR CODE BELOW THIS LINE
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img)

    enh_bri = ImageEnhance.Brightness(pil_image)
    brightness = 1.0
    image_brightened = enh_bri.enhance(brightness)

    enh_col = ImageEnhance.Color(image_brightened)
    color = 2.5
    image_colored = enh_col.enhance(color)

    enh_con = ImageEnhance.Contrast(image_colored)
    contrast = 1.1
    image_contrasted = enh_con.enhance(contrast)

    enh_sha = ImageEnhance.Sharpness(image_contrasted)
    sharpness = 5.0
    image_sharped = enh_sha.enhance(sharpness)
    
    enh_bri = ImageEnhance.Brightness(image_sharped)
    brightness = 1.1
    image_brightened = enh_bri.enhance(brightness)
    
    smoothenedImage = image_brightened.filter(ImageFilter.SMOOTH)

    image_array = np.array(smoothenedImage)
    output_BGR = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

    outputImg = output_BGR
    # END OF YOUR CODE
    #########################################################################
    return outputImg
    
