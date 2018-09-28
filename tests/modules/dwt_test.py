'Test Definition for Compression methods'
import unittest
import os
import numpy as np
from src.utils import load_img
from src.compression import (
    rgb_to_yuv, \
    yuv_to_rgb, \
    extract_rgb_coeff, \
    img_from_dwt_coeff, \
    recontract_img_from_dwt_coef, \
    creat_lost_LH_HL_HH_dwt_coef, \
    creat_lost_HL_HH_dwt_coef, \
    creat_lost_HH_dwt_coef
)

FOLDER = 'data'
FILENAME = 'lena.png'

class CompressionTest(unittest.TestCase):
    'Units test for compression methods'
    def test_rgb_to_yuv(self):
        'it should return an Image Type after conversion'
        img = load_img(os.path.join(FOLDER, FILENAME))
        img_yuv = rgb_to_yuv(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')

    def test_yuv_to_rgb(self):
        'it should return an Image Type after conversion'
        img = load_img(os.path.join(FOLDER, FILENAME))
        img_yuv = yuv_to_rgb(img)
        self.assertEqual(type(img_yuv).__name__, 'Image')

    def test_extract_rgb_coeff(self):
        'it should return a Tuple of coefficient per each channel (RGB)'
        img = load_img(os.path.join(FOLDER, FILENAME))
        (c_r, c_g, c_b) = extract_rgb_coeff(img)
        self.assertTrue(c_r[0] is not None)
        self.assertTrue(c_r[1] is not None)
        self.assertTrue(c_g[0] is not None)
        self.assertTrue(c_g[1] is not None)
        self.assertTrue(c_b[0] is not None)
        self.assertTrue(c_b[1] is not None)

    def test_img_from_dwt_coeff(self):
        'TODO'
        img = load_img(os.path.join(FOLDER, FILENAME))
        coeff = extract_rgb_coeff(img)
        img_new = img_from_dwt_coeff(coeff)
        img_new.save('/home/jiewend/download/a_4component.png')
        return
    def test_recontract_img_from_dwt_coef(self):
        img = load_img(os.path.join(FOLDER, FILENAME))
        coeff = extract_rgb_coeff(img)
        coeff_copy = coeff
        
        img_new = recontract_img_from_dwt_coef(coeff)
    def test_creat_lost_dwt_coef(self):
        img = load_img(os.path.join(FOLDER, FILENAME))
        coeff = extract_rgb_coeff(img)

        coff_lost = creat_lost_LH_HL_HH_dwt_coef(coeff, 1)
        img_new = recontract_img_from_dwt_coef(coff_lost)
        img_new.save('/home/jiewend/download/a_re_lost_LH_HL_HH.png')

        coff_lost = creat_lost_HL_HH_dwt_coef(coeff, 1)
        img_new = recontract_img_from_dwt_coef(coff_lost)
        img_new.save('/home/jiewend/download/a_re_lost_HL_HH.png')

        coff_lost = creat_lost_HH_dwt_coef(coeff, 1)
        img_new = recontract_img_from_dwt_coef(coff_lost)
        img_new.save('/home/jiewend/download/a_re_lost_HH.png')



