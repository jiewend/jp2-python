import os

'Converts Image Matrix from RGB to YUV'
def RGB_to_YUV(img):
    yuv_img = img.convert('RGB')
    width, height = img.size
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
        yuv_img.putpixel((x, y) , (int(Y),int(CB),int(CR)))
    return  yuv_img

def YUV_to_RGB():
    return 42
