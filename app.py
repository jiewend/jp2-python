'Main Module'
#!/usr/bin/python
import os
import src.utils as util
import src.compression as dwt
import src.windows as win

def run():
    folder = 'data'
    filename = 'lena.png'
    img = util.loadImg(os.path.join(folder, filename))
    (c_r, c_g, c_b) = dwt.extract_rgb_coeff(img)
    print (len(c_r[0]))

if __name__ == '__main__':
    run()
