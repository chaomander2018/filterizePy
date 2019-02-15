# Copyright (c) 2019 Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# Feburary 2019
# This script tests the function from mirror.py.

# This script tests the mirror function of the filterizePy package.
import sys
sys.path.append('../../')

from skimage import io
import numpy as np
import pytest
from filterizePy.mirror import mirror

input_img = "../../img/test_original.jpg"
mirror(input_img)
input_img = io.imread('../../img/test_original.jpg')
output_img = io.imread('../../img/mirrored_test_original.jpg')

def test_flip_same_size(input_img, output_img):
    # checks input and output size
    assert input_img.shape == output_img.shape, "Input and output dimensions do not match"

def test_flip_column_flip(input_img, output_img):
    # first and last column should have the same pixels
    assert np.all(np.abs(input_img[:,0,:] - output_img[:,-1,:]) < 20), "First and last pixel columns do not match"

def test_flip_column_flip_mid(input_img, output_img):
    # middle column should stay the same, the cases are different for even and odd dimensioned images
    m,n,d = input_img.shape
    input_img = np.array(input_img, dtype=np.float64)
    output_img = np.array(output_img, dtype=np.float64)

    if n % 2 == 0:
        mid = n//2
        assert np.all(np.abs(input_img[:,mid,:] - output_img[:,mid-1,:]) < 20)
    else:
        mid = n//2
        assert np.all(np.abs(input_img[:,mid,:] - output_img[:,mid,:]) < 20)

def reversed_input_img():
    with pytest.raises(FileNotFoundError):
        mirror("not a file path")

def test_flip_invalid_input():
    with pytest.raises(AttributeError):
        mirror(123)

def test_flip_invalid_input_2():
    with pytest.raises(TypeError):
        mirror()

reversed_input_img()
test_flip_invalid_input()
test_flip_invalid_input_2()
test_flip_same_size(input_img, output_img)
test_flip_column_flip(input_img, output_img)
test_flip_column_flip_mid(input_img, output_img)
