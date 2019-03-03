# Copyright (c) 2019 Chao Wang, Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# This script sharpens an image.
# Input  : A path to an image in either .png, .jpeg, .gif, .bmp, or .jpg format
# Output : A path to a sharpened .png .jpeg, .gif, .bmp, or .jpgimage

import numpy as np
import skimage.io
from scipy.signal import convolve2d
#from keras.preprocessing.image import img_to_array, load_img
import matplotlib.pyplot as plt
import os
from PIL import Image

def sharpen_image(input_path):
    """This function sharpens an image.

    This function read the input image path and apply the sharpen convolution filter to the image.
    The output image should be saved under the same file path.

    Parameters
    ----------
    input_img: string
    A file path to a image. The image should be either .png, .jpeg, .gif, .bmp, or .jpg.

    Returns
    -------
    output_img: string
    An image file which have the same file format as the inut image.
    This is the sharpened image, it has the same dimension and file type as the input_img

    Example
    -------
    sharpen("../img/test_image.png")

    Returns"../img/sharpened_test_image.png"
    """
    # Read the image
    try:
        input_img = skimage.io.imread(input_path)
        # input_img = Image.open(input_path).convert('RGB')
    except FileNotFoundError:
        print("Could not find your file, please try again")
        raise
    except AttributeError:
        print("Please provide a string as a paht for the input file")
        raise

    #
    # except OSError:
    #     print("The inputfile is not an image")
    #     raise
    # except Exception as e:
    #     print("General Error:")
    #     raise


    # breakdown to 3 images
    r_img = input_img[:, :, 0]
    g_img = input_img[:, :, 1]
    b_img = input_img[:, :, 2]



    # Construct the sharpen filter
    ft = np.zeros((3,3))
    ft[1,1] = 4.5
    ft[0,1]=ft[1,0]=ft[1,2]=ft[2,1]=-0.75

    # Apply sharpen filter to the red image
    r_output_img = convolve2d(r_img, ft , boundary='symm', mode='same')
    r_output_img = np.maximum(0, r_output_img)
    r_output_img = np.minimum(1, r_output_img)


    # Apply sharpen filter to the green image
    g_output_img = convolve2d(g_img, ft , boundary='symm', mode='same')
    g_output_img = np.maximum(0, g_output_img)
    g_output_img = np.minimum(1, g_output_img)


    # Apply sharpen filter to the blue image
    b_output_img = convolve2d(b_img, ft , boundary='symm', mode='same')
    b_output_img = np.maximum(0, b_output_img)
    b_output_img = np.minimum(1, b_output_img)


    # put back the three sharpened image
    output_img = np.dstack((r_output_img, g_output_img,b_output_img))

    # Get the input image path and generate the output path
    index = input_path.rfind("/") + 1
    output_path = input_path[:index] + "sharpened_" + input_path[index:]

    # save the output image to the same file path as the input image file path
    skimage.io.imsave(output_path, output_img)
    # return the output image file path
    return output_path
