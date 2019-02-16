<img src="https://filterize.net/wp-content/uploads/2018/02/logo_text_bottom-2.png" align="right" height="190" width="220"/>

## filterizePy
This is a comprehensive image filtering package based in Python.

**Date:** 2019-02-16

**License:** [MIT](https://opensource.org/licenses/MIT)

#### Authors

|Contributors |Jack Yang| Akansha Vashisth |Chao Wang|
|---|---|---|----|
|github handle|[@jackattackyang](https://github.com/jackattackyang)|[@akanshaVashisth](https://github.com/akanshaVashisth)|[@chaomander2018](https://github.com/chaomander2018)|

### Usage and Installation

`pip install git+https://github.com/UBC-MDS/filterizePy` <br>
`from filterizePy import *`

### Overview

This is a Collaborative Software Development Project in which we will be working on three image processing filters using convolutions.

![theme](img/theme.png)

### Functions  (see details in milestone 1 writeup)

- #### Green Color Filter `greenscale()`
This green color filter converts the original image to a green scaled image.
Please see the original image and processed image below.

- #### Sharpen Filter `sharpen_image()`
This sharpen filter highlights edges and fine details in an image.

- #### Mirror Filter `mirror()`
This mirror filter function will use convolution to convert the original image to a mirrored image i.e. the left side of the image will be transformed into the right side and the right side of the original image will be transformed into the left side.

## Test instructions:

## package Dependencies:
PIL
skimage
numpy
