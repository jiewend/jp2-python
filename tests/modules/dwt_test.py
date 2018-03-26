'-'
import unittest
import os
from src.utils import loadImg
from src.compression import rgb_to_yuv

class CompressionTest(unittest.TestCase):
    'it should return an Image Type after conversion'
    def test_rgb_to_yuv(self):
        '-'
        folder = 'data'
        filename = 'lena.png'
        img = loadImg(os.path.join(folder, filename))
        img_yuv = rgb_to_yuv(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')
