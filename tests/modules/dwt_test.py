'-'
import unittest
import os
from src.utils import loadImg
from src.compression import rgb_to_yuv, yuv_to_rgb, extract_rgb_coeff

folder = 'data'
filename = 'lena.png'

class CompressionTest(unittest.TestCase):
    'it should return an Image Type after conversion'
    def test_rgb_to_yuv(self):
        '-'
        img = loadImg(os.path.join(folder, filename))
        img_yuv = rgb_to_yuv(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')
    
    'it should return an Image Type after conversion'
    def test_yuv_to_rgb(self):
        '-'
        img = loadImg(os.path.join(folder, filename))
        img_yuv = yuv_to_rgb(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')
    
    def test_extract_rgb_coeff(self):
        '-'
        img = loadImg(os.path.join(folder, filename))
        (width, height) = img.size
        (c_r, c_g, c_b) = extract_rgb_coeff(img)
        self.assertTrue(c_r[0] is not None)
        self.assertTrue(c_r[1] is not None)
        self.assertTrue(c_g[0] is not None)
        self.assertTrue(c_g[1] is not None)
        self.assertTrue(c_b[0] is not None)
        self.assertTrue(c_b[1] is not None)
        
    
