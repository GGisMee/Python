from PIL import Image
import os
import numpy as np
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))


image_obj = Image.open('cat1.png')
image_obj.show()

img_rgb = np.array(image_obj.convert('RGB'))
img_rgb.shape
