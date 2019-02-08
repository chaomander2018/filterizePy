# This function sharpens an image.
# Input  : An image in .png, .jpeg,.gif,.bmp, .jpg format
# Output : A sharpened image in the same format as the input image file type

def sharpen(input_img):
    """This function sharpens an image.

    This function read the input image path and apply the sharpen convolution filter to the image.
    The output image should be saved under the same file path.

    Parameters
    ----------
    input_img: A img file path
    The image should be either .png, .jpeg,.gif, .bmp, or .jpg.

    Returns
    -------
    output_img: an image file which have the same file format as the inut image.
    This is the sharpened image, it has the same dimension and file type as the input_img

    Example
    -------
    sharpen("../img/0.png")
    """
    input_img = skimage.io.imread(input_img)
    # Construct sharpen filter
    ft = np.zeros((3,3))
    ft[1,1] = 5
    ft[0,1]=ft[1,0]=ft[1,2]=ft[2,1]=-2

    # Apply sharpen filter to the image, this function will be complete by milestone 2.
    output_img = input_img
    skimage.io.imsave("../img/sharpened_img.png", output_img)
