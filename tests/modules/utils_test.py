'-'
import unittest
import os
from src.utils import loadImg

class UtilTest(unittest.TestCase):
    '-'
    def test_load_png_file(self):
        '-'
        # case 1 (it should work):
        img = loadImg(os.path.join('data', 'lena.png'))
        self.assertEqual(type(img).__name__, 'PngImageFile')
        # case 2 (it should raise an exception):
        img = loadImg(os.path.join('data', 'dummy_file.png'))
        self.assertEqual(type(img).__name__, 'NoneType')
