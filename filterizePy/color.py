# Copyright (c) 2019 Akansha Vashisth, Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# This script converts an image into green colored image.
# Input  : An image in .png, .jpeg,.gif,.bmp, .jpg format
# Output : A green-colored image in the same format as the input image file type.

def color(input_img):
    """This function converts an image into green colored image.
    This function read the input image path and apply the convolution filter to the image.
    The output image should be saved under the same file path.
    Parameters
    ----------
    input_img: A img file path
    The image should be either .png, .jpeg,.gif, .bmp, or .jpg.
    
    Returns
    -------
    output_img: an image file which have the same file format as the inut image.
    This is the sharpened image, it has the same dimension and file type as the input_img
    """
   