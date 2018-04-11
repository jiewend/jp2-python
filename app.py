'Main Module'
#!/usr/bin/python
import os
import src.utils as util
import src.compression as dwt
import src.windows as win
import numpy as np

FOLDER = 'data'
RIGHT_FILENAME = 'lena.png'

def run():
    img = util.load_img(os.path.join(FOLDER, RIGHT_FILENAME))
    #print (dwt.extract_rgb_coeff(img))

if __name__ == '__main__':
    run()
