# Copyright (c) 2019 Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# Feburary 2019
# This script tests the mirror function of the filterizePy package.
# pytest test_mirror.py -s -v

import sys
import os
sys.path.append(os.getcwd())
import skimage.io
import numpy as np
import pytest
from filterizePy.mirror import mirror

def setup_module(module):
    module.Test_mirror.input_img = "test_img/test_original.jpg"
    mirror(module.Test_mirror.input_img)
    module.Test_mirror.input_img = skimage.io.imread('test_img/test_original.jpg')
    module.Test_mirror.output_img = skimage.io.imread('test_img/mirrored_test_original.jpg')
    print("----------RUNNNINNNG------------")

def teardown_module(module):
    print("----------ENDDDINNNG------------")

class Test_mirror:

    @pytest.mark.main_
    def test_flip_same_size(self):
        # checks input and output size
        assert self.input_img.shape == self.output_img.shape, "Input and output dimensions do not match"

    @pytest.mark.main_
    def test_flip_column_flip(self):
        # first and last column should have the same pixels
        self.input_img = np.array(self.input_img, dtype=np.float64)
        self.output_img = np.array(self.output_img, dtype=np.float64)

        assert np.all(np.abs(self.input_img[:,0,:] - self.output_img[:,-1,:]) < 20), "First and last pixel columns do not match"

    @pytest.mark.main_
    def test_flip_column_flip_mid(self):
        # middle column should stay the same, the cases are different for even and odd dimensioned images
        self.input_img = np.array(self.input_img, dtype=np.float64)
        self.output_img = np.array(self.output_img, dtype=np.float64)
        m,n,d = self.input_img.shape

        if n % 2 == 0:
            mid = n//2
            assert np.all(np.abs(self.input_img[:,mid,:] - self.output_img[:,mid-1,:]) < 20)
        else:
            mid = n//2
            assert np.all(np.abs(self.input_img[:,mid,:] - self.output_img[:,mid,:]) < 20)

    @pytest.mark.raise_
    def test_reversed_input_1(self):
        with pytest.raises(FileNotFoundError):
            mirror("not a file path")

    @pytest.mark.raise_
    def test_mirror_invalid_input_2(self):
        with pytest.raises(AttributeError):
            mirror(123)
