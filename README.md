<img src="https://filterize.net/wp-content/uploads/2018/02/logo_text_bottom-2.png" align="right" height="190" width="220"/>

## filterizePy
This is a comprehensive image filtering package based in Python.

**Date:** 2019-02-16

**License:** [MIT](https://opensource.org/licenses/MIT)

#### Authors

|Contributors |Jack Yang| Akansha Vashisth |Chao Wang|
|---|---|---|----|
|github handle|[@jackattackyang](https://github.com/jackattackyang)|[@akanshaVashisth](https://github.com/akanshaVashisth)|[@chaomander2018](https://github.com/chaomander2018)|

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


## Installation and Usage

`pip install git+https://github.com/UBC-MDS/filterizePy` <br>
`from filterizePy import *`

1. **greenscale(input_path)**

Argument:
- ```input_path```: path to input image
- *Example*: ```greenscale("./img.jpg")```

2. **sharpen_image(input_path)**

Argument:
- ```input_path```: path to input image
- *Example*: ```sharpen_image("./img.jpg")```

3. **mirror(input_path)**

Arguments:
- ```input_path```: path to input image
- *Example*: ```mirror("./img.jpg")```


## Test instructions:


## Package Dependencies:
- PIL
- skimage
- numpy


## Reference:
Image Sources:
- [filterize.net](https://filterize.net/wp-content/uploads/2018/02/logo_text_bottom-2.png)
- [quickmeme](http://www.quickmeme.com/img/2f/2f516b33efd7251b57bad254f1688131458e13d005972810676ea9622a6c4d29.jpg)