# Copyright 2019 Akansha Vashisth
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# February 2019
# This script tests color function of filterizePy package.
import pytest
import numpy as np
import pandas as pd
import os
import imghdr
import skimage.io
from filterizePy.greenscale import greenscale

def test_greenscale_white():
    # White image testing
    test_img = np.array([[[255, 255, 255],[255, 255, 255],[255, 255, 255]] ,
                          [[255, 255, 255],[255, 255, 255],[255, 255, 255]],
                          [[255, 255, 255],[255, 255, 255],[255, 255, 255]],
                          [[255, 255, 255],[255, 255, 255],[255, 255, 255]],
                          [[255, 255, 255],[255, 255, 255],[255, 255, 255]]], dtype = "uint8")
    gs_test_img = np.array([[[  0, 230, 0],[  0, 230, 0],[  0, 230,  0]],
                             [[  0, 230, 0],[  0, 230, 0],[  0, 230,  0]],
                             [[  0, 230, 0],[  0, 230, 0],[  0, 230,  0]],
                             [[  0, 230, 0],[  0, 230, 0],[  0, 230,  0]],
                             [[  0, 230, 0],[  0, 230, 0],[  0, 230,  0]]], dtype = "uint8")

    greenscale("../../img/test_img.png")
    output_expected = skimage.io.imread("../../img/gs_test_img.png")
    assert np.array_equal(output_expected, gs_test_img), "The greenscale function does not work properly."


def test_greenscale_black():
    # Black image testing
    test_img_black = np.array([[[0, 0, 0]]], dtype = "uint8")
    gs_test_img_black = np.array([[[0, 0, 0]]], dtype = "uint8")

    greenscale("../../img/test_img_black.jpeg")
    output_expected = skimage.io.imread("../../img/test_img_black.jpeg")
    assert np.array_equal(output_expected, gs_test_img_black), "The greenscale function does not work properly."


def test_same_size():
    # Checking input and output size
    input_img = "../../img/test_original.jpg"
    greenscale(input_img)
    input_img = skimage.io.imread('../../img/test_original.jpg')
    output_img = skimage.io.imread('../../img/gs_test_original.jpg')
    assert input_img.shape == output_img.shape, "Input and output dimensions do not match"


def check_output_type():
    input_img = "../../img/test_original.jpg"
    greenscale(input_img)
    input_img = skimage.io.imread('../../img/test_original.jpg')
    output_img = skimage.io.imread('../../img/gs_test_original.jpg')
    assert imghdr.what(output_img) in ['png','jpeg','gif','bmp','jpg'] and imghdr.what(output_img)==imghdr.what(input_img),"The output image has a different file format"

def test_input_img():
    input_img = "../../img/test_original.jpg"
    greenscale(input_img)
    input_img = skimage.io.imread('../../img/test_original.jpg')
    output_img = skimage.io.imread('../../img/gs_test_original.jpg')
    with pytest.raises(FileNotFoundError):
        greenscale("not a file path")

def test_invalid_input():
    with pytest.raises(AttributeError):
        greenscale(123)

def test_invalid_input_type_error():
    with pytest.raises(FileNotFoundError):
        greenscale("Hi")
