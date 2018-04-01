# pylint: disable=C0103,E0401,W0631
'compression methods'
import pywt
import numpy

def rgb_to_yuv(img):
    '-'
    yuv_img = img.convert('RGB')
    (width, height) = img.size
    for x in range(width):
        for y in range(height):
            (r, g, b) = yuv_img.getpixel((x, y))
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        CB = - 0.168935 * r + - 0.331665 * g + 0.50059 * b + 128
        CR = 0.499813 * r - 0.4187 * g + - 0.081282 * b + 128
        Y = 255 if (Y >= 255) else Y
        Y = 0 if (Y <= 0) else Y
        CB = 255 if (CB >= 255) else CB
        CB = 0 if (CB <= 0) else CB
        CR = 255 if (CR >= 255) else CR
        CR = 0 if (CR <= 0) else CR
        yuv_img.putpixel((x, y), (int(Y), int(CB), int(CR)))
    return yuv_img

def yuv_to_rgb(img):
    '-'
    (width, height) = img.size
    rgb_img = img.copy()
    for x in range(width):
        for y in range(height):
            (Y, CB, CR) = img.getpixel((x, y))
        R = Y + 1.402 * (CR - 128)
        G = Y - 0.34414 * (CB - 128) - 0.71414 * (CR - 128)
        B = Y + 1.772 * (CB -128)
        R = 255 if (R >= 255) else R
        R = 0 if (R <= 0) else R
        G = 255 if (G >= 255) else G
        G = 0 if (G <= 0) else G
        B = 255 if (B >= 255) else B
        B = 0 if (B <= 0) else B
        rgb_img.putpixel((x, y), (int(R), int(G), int(B)))
    return  rgb_img

def rgb_to_grayscale(img):
    'Converts an Image to Greyscale'
    width, height = img.size
    res = img.copy()
    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            gs = int((r + g + b) / 3)
            res.putpixel((i, j), (gs, gs, gs))
    return res

def extract_rgb_coeff(img):
    'Extracts RGB coefficients of a given Image'
    (width, height) = img.size
    img = img.copy()

    mat_r = numpy.empty((width, height))
    mat_g = numpy.empty((width, height))
    mat_b = numpy.empty((width, height))

    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            mat_r[i, j] = r
            mat_g[i, j] = g
            mat_b[i, j] = b

    # coeffs_r: cA,(cH,cV,cD)
    coeffs_r = pywt.dwt2(mat_r, 'haar')
    # coeffs_g: cA,(cH,cV,cD)
    coeffs_g = pywt.dwt2(mat_g, 'haar')
    # coeffs_b: cA,(cH,cV,cD)
    coeffs_b = pywt.dwt2(mat_b, 'haar')
    return (coeffs_r, coeffs_g, coeffs_b)
