import numpy as np
from PIL import Image
from time import sleep

'''------------------------------------------------
How to convert an image into an array of 0 and 1
get 0 for white
1 for black
------------------------------------------------'''

def map_to_array(image):
    "input image and return array"

    img = Image.open(image)   
    img = img.convert(mode="1", dither=Image.NONE)
    array = np.array(img, dtype=np.uint8)
    print(array)
    return array

if __name__ == "__main__":
    map_to_array("map1.png")
    sleep(5)






















