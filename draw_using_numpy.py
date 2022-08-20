import numpy as np
from PIL import Image

# Create a 3-dimensional array of Integers
data = np.zeros((6, 4, 3), dtype=np.uint8)


# Change the array values from 0 to specific values.
data[0:2] = [255, 153, 51]
data[2:4] = [255, 255,255]
data[4:] = [19, 136, 8]

data[2:4, 1:3] = [0, 0, 128]


# Create an image from the pixel values listed in the array.
img = Image.fromarray(data, 'RGB')
img.save('canvas1.png')
