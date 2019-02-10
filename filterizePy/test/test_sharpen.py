# Copyright 2019 Chao Wang, Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# February 2019
# This script tests the sharpen function of filterizePy package.


import numpy as np
import pandas as pd
import os
import imghdr
import skimage.io
from PIL import Image
from filterizePy import sharpen

def check_input_type(input_img):
    """
    This function checks the input image format is one of the valid image formats.

    """
    assert imghdr.what(input_img) in ['png','jpeg','gif','bmp','jpg'] , "The input image format is incorrect, try another format"


def check_output_type(input_img, sharpen(input_img)):
    """
    This function checks the output image format is one of the valid image formats,
    and it matches the input image format
    """
    assert imghdr.what(output_img) in ['png','jpeg','gif','bmp','jpg'] and imghdr.what(output_img)==imghdr.what(input_img),"The output image has a different file format"


def check_output_dimension(input_img, sharpen(input_img)):
    """
    This function checks whether the output image has the same dimension as the input image.
    """
    input_img = skimage.io.imread(input_img)
    output_img= skimage.io.imread(sharpen(input_img))
    in_width, in_height,in_rgb = input_img.shape
    out_width, out_height,out_rgb = output_img.shape
    assert in_width == out_width and in_height==out_height
