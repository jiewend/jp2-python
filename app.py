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

    print (img.getpixel(0))

    if img != None:
        img_yuv = dwt.RGB_to_YUV(img)

if __name__ == '__main__':
    run()
