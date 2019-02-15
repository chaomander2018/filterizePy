import numpy as np
import skimage.io

def greenscale(input_path):
    '''
    This function converts an image into green colored image.
    Input: input_path: string, path for the input image file
           output_path: string, path for the output image file
    Output: an image file at the specified output path
    '''
    # exception handling
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
    height = img.shape[0]
    width = img.shape[1]

    img_gs = np.zeros(img.shape, dtype = "uint8")

    for i in range(height):
        for j in range(width):
            R = img[i][j][0]
            G = img[i][j][1]
            B = img[i][j][2]

            green = round(0.5*G)

            img_gs[i][j][1] = green

            
    return skimage.io.imsave(output_path, img_gs)
