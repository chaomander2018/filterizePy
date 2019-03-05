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

Over 3.5 million photos were shared every minute in 2016 [(Deloitte)](https://www2.deloitte.com/uk/en/pages/press-releases/articles/3-point-5-million-photos-shared-every-minute.html). Visual conversations are a huge part of our lives. All social media feeds are filled with digital stories on Instagram, Facebook, Snapchat, and Twitter. Digital image processing is an important social media metric. We were driven to design a package for image processing and filtering. This is a Collaborative Software Development Project in which we have started working on three image processing filters using convolutions.

### Functions

- #### Green Color Filter `greenscale()`
This green color filter converts the original image to a green scaled image.
Please see the original image and processed image below.
<img src="img/greenscale.png" style="width:700px;height:200px">

- #### Sharpen Filter `sharpen_image()`
This sharpen filter highlights edges and fine details in an image.
![](img/sharpen.png)

- #### Mirror Filter `mirror()`
This mirror filter function will use convolution to convert the original image to a mirrored image i.e. the left side of the image will be transformed into the right side and the right side of the original image will be transformed into the left side.
![](img/mirror.png)

### Python Ecosystem
There are many packages that perform image processing for accessorizing, color enhancement or special effects. In fact, the idea for this project came from the MDS cohort from last year. The intent behind this project is to build onto the intuition behind convolutional neural networks and how image filtering works while working on a relevant and practical project.
* [MDS package 2018](https://github.com/UBC-MDS/InstaR/tree/v4.0)
* [Zomato Android filter](https://github.com/Zomato/AndroidPhotoFilters)

### Installation

For installing this package, run the following command on your terminal:

`pip install git+https://github.com/UBC-MDS/filterizePy`

### Usage

`from filterizePy.greenscale import greenscale`

`from filterizePy.sharpen_image import sharpen_image`

`from filterizePy.mirror import mirror`

**greenscale(input_path)**

  - `input_path`: Input image path
  - *Example*: `greenscale.greenscale(input_path)`


**sharpen_image(input_path)**

  - `input_path`: Input image path
  - *Example*: `sharpen.sharpen_image(input_path)`


**mirror(input_path)**

  - `input_path`: Input image path
  - *Example*: `mirror.mirror(input_path)`

### Testing

`pytest`

![](img/pytest_result.png)

`py.test filterizePy/test/ --cov=filterizePy/ `

![](img/python_coverage.png)

### Package Dependencies:
- PIL
- skimage
- numpy


### Reference:
Image Sources:
- [filterize.net](https://filterize.net/wp-content/uploads/2018/02/logo_text_bottom-2.png)
- [quickmeme](http://www.quickmeme.com/img/2f/2f516b33efd7251b57bad254f1688131458e13d005972810676ea9622a6c4d29.jpg)
