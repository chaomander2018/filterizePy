# Copyright (c) 2019 Master of Data Science at the University of British Columbia
# Licensed under the MIT License (the "License").
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://mit-license.org

# Feburary 2019
# This function mirrors an image.
# Input  : An image in .png, .jpeg,.gif,.bmp, .jpg format
# Output : A mirrored image in the same format as the input image file type

# Example input path: "../../img/mirror_img.png"
# Example output path: "../../img/mirrored_mirror_img.png"

from skimage import io
import numpy as np

def mirror(input_path):

    try:
        input_img = io.imread(input_path)
    except FileNotFoundError:
        print("Please enter a valid file path")
        raise
    except AttributeError:
        print("Please entire a valid path as a string")
        raise
    # except Exception as error:
    #     print(error)
    #     raise

    # Regex that customizes output file name
    index = input_path.rfind("/") + 1
    output_path = input_path[:index] + "mirrored_" + input_path[index:]

    io.imsave(output_path, input_img[:,::-1,:])

# if __name__ == "__main__":
#     mirror(sys.argv[1])
