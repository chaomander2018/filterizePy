# Copyright (c) 2019 Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# Feburary 2019
# This script tests the function from mirror.py.

# This script tests the mirror function of the filterizePy package.

from skimage import io
import pytest
import numpy as np
from filterize import mirror

input_img = io.imread('../img/input_image.png')
mirror(input_img)
output_img = io.imread('../img/mirror_img.png')

def test_flip_same_size(input_img, output_img):
    # checks input and output size
    assert input_img.shape == output_img.shape, "Input and output dimensions do not match"

def test_flip_column_flip(input_img, output_img):
    # first and last column should have the same pixels
    assert np.array_equal(input_img[:,0,:], output_img[:,-1,:]), "First and last pixel columns do not match"

def test_flip_column_flip_mid(input_img, output_img):
    # middle column should stay the same, the cases are different for even and odd dimensioned images
    m,n,d = input_img.shape

    if n % 2 == 0:
        mid = n//2
        assert np.array_equal(input_img[:,mid,:], output_img[:,mid-1,:])
    else:
        mid = n//2
        assert np.array_equal(input_img[:,mid,:], output_img[:,mid,:]), "Error in middle transform column"

def test_flip_file_path():
    with pytest.raises(FileNotFoundError):
        mirror("not a file path")

def test_flip_invalid_input():
    with pytest.raises(AttributeError):
        mirror(123)

def test_flip_invalid_input():
    with pytest.raises(TypeError):
        mirror()

def test_flip_invalid_input():
    with pytest.raises(SyntaxError):
        mirror(,)
