'Test Definition for Utility methods'
import unittest
import os
from src.utils import load_img

FOLDER = 'data'
RIGHT_FILENAME = 'lena.png'
WRONG_FILENAME = 'dummy_file.png'

class UtilTest(unittest.TestCase):
    'Units test for utility methods'
    def test_load_png_file(self):
        'it should return an Image Type if file exists and is an Image file'
        # case 1 (it should return PngImageFile):
        img = load_img(os.path.join(FOLDER, RIGHT_FILENAME))
        self.assertEqual(type(img).__name__, 'PngImageFile')
        # case 2 (it should return NoneType):
        img = load_img(os.path.join(FOLDER, WRONG_FILENAME))
        self.assertEqual(type(img).__name__, 'NoneType')
