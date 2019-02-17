import numpy as np
import skimage.io
from PIL import Image

def greenscale(input_path):
    '''
    This function converts an image into green colored image.
    Input: input_path: string, path for the input image file
           output_path: string, path for the output image file
    Output: an image file at the specified output path
    
    Example: greenscale("../img/test_image.png")
    '''
    
    # Exception handling
    try:
        img = skimage.io.imread(input_path)
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except FileNotFoundError:
        print("The input file does not exist.")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise
    
    index = input_path.rfind("/") + 1
    output_path = input_path[:index] + "gs_" + input_path[index:]
    
    # Converting any format(like RGBA) to RGB
    img = Image.open(input_path).convert('RGB')
    
    img = np.asarray(img)
    width, height, d = img.shape
    img_gs = np.zeros(img.shape)

    for i in range(height):
        for j in range(width):
            # Assigning new green pixels
            img_gs[j][i][1] = round(0.9*img[j][i][1])
            
    out = Image.fromarray(np.uint8(img_gs))
    out.save(output_path)
