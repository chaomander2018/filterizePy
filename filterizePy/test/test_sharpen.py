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
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from filterizePy.sharpen import sharpen_image
import pytest
from keras.preprocessing.image import img_to_array, load_img



test_path = "img/mirror.png"

def test_input_type():
    """
    This function checks the input image format is one of the valid image formats.
    """
    assert imghdr.what("img/mirror.png") == 'png', "Not a png file, please try again"

def test_output_type():
    """
    This function checks the output image format is one of the valid image formats.
    """
    output_path = sharpen_image("img/mirror.png")
    assert imghdr.what(output_path) == imghdr.what("img/mirror.png"), "Not a png file, please try again"



def test_output_dimension():
     """
     This function checks whether the output image has the same dimension as the input image.
     """
     input_img = skimage.io.imread("img/mirror.png")
     output_img= skimage.io.imread(sharpen_image("img/mirror.png"))
     in_width, in_height,in_rgb = input_img.shape
     out_width, out_height,out_rgb = output_img.shape
     assert in_width == out_width and in_height==out_height, "dimension has changed, something is wrong"

def test_sharpened_effect():
    """
    This function test that the sharpened effect actually implemented on the inpug image.
    """
    input_img = skimage.io.imread("img/mirror.png")
    output_img= skimage.io.imread(sharpen_image("img/mirror.png"))
    in_width, in_height,in_rgb = input_img.shape
    out_width, out_height,out_rgb = output_img.shape
    assert in_rgb != out_rgb, "no effect applied, something is wrong"
