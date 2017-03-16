from PIL import Image
import pywt
import numpy

# load an image file
def loadImg(path):
    return Image.open(path)

#Take an image in the RGB space
#Returns a YCbCr image
def RGBtoYUV(img):
    yuv_img = img.convert('RGB')
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r,g,b = yuv_img.getpixel((x,y))
	    Y = 0.299 * r + 0.587 * g + 0.114  * b
	    CB = - 0.168935 * r + - 0.331665 * g + 0.50059 * b + 128
	    CR = 0.499813 * r - 0.4187 * g + - 0.081282 * b + 128
	    Y = 255 if (Y >= 255) else Y
	    Y = 0 if (Y <= 0) else Y
	    CB = 255 if (CB >= 255) else CB
	    CB = 0 if (CB <= 0) else CB	
	    CR = 255 if (CR >= 255) else CR
	    CR = 0 if (CR <= 0) else CR
	    yuv_img.putpixel((x,y) , (int(Y),int(CB),int(CR)))
    return  yuv_img

#Take an image in the YCbCr space
#Returns a RGB image
def YUVtoRGB(img):
    width,height = img.size
    rgb_img = img.copy()
    for x in range(width):
        for y in range(height):
            Y,CB,CR = img.getpixel((x,y))
	    R = Y + 1.402 * ( CR - 128 )
	    G = Y - 0.34414 * (CB - 128 ) - 0.71414 * (CR - 128 )
	    B = Y + 1.772 * (CB -128 )
	    R = 255 if (R >= 255) else R
	    R = 0 if (R <= 0) else R
	    G = 255 if (G >= 255) else G
	    G = 0 if (G <= 0) else G	
	    B = 255 if (B >= 255) else B
	    B = 0 if (B <= 0) else B
	    rgb_img.putpixel((x,y) , (int(R),int(G),int(B)))
    return  rgb_img

#Convert the image to a greyscale space
def RGBtoGray(image):
    width, height = image.size
    img = image.copy() 
    pixel = img.load() 
    for i in range(width):
        for j in range(height):
            (r, g, b) = pixel[i,j]
            gs = int((r + g + b) / 3)
            pixel [i, j] = (gs, gs, gs)
    return img

def pixelsRed(image):
    width, height = image.size
    img = image.copy()
    pixel = img.load()
    matriz = numpy.empty((width, height))
    for i in range(width):
        for j in range(height):
            (r,g,b) = image.getpixel((i,j))
            #We are only processing red here
            matriz[i,j] = r

    coeffs = pywt.dwt2(matriz, 'haar')
    cA,(cH,cV,cD) = coeffs
    return coeffs

def pixelsGreen(image):
    width, height = image.size
    img = image.copy()
    pixel = img.load()
    matriz = numpy.empty((width, height))
    for i in range(width):
        for j in range(height):
            (r,g,b) = image.getpixel((i,j))
            #We are only processing green here
            matriz[i,j] = g

    coeffs = pywt.dwt2(matriz, 'haar')
    cA,(cH,cV,cD) = coeffs
    return coeffs

def pixelsBlue(image):
    width, height = image.size
    img = image.copy()
    pixel = img.load()
    matriz = numpy.empty((width, height))
    for i in range(width):
        for j in range(height):
            (r,g,b) = image.getpixel((i,j))
            #We are only processing blue here
            matriz[i,j] = b
    coeffs = pywt.dwt2(matriz, 'haar')
    cA,(cH,cV,cD) = coeffs
    #print cA.size

    return coeffs

def idwt(coR,coG,coB,img):
    iR = pywt.idwt2(coR,'haar')
    iG = pywt.idwt2(coG,'haar')
    iB = pywt.idwt2(coB,'haar')
    pixel = img.load()
    width,height= img.size
    for i in range(width):
        for j in range(height):
            rComp = int(iR[i,j])
            gComp = int(iG[i,j])
            bComp = int(iB[i,j])
            pixel[i,j]= (rComp,gComp,bComp)
        #print pixel[i,j]
    return pixel


''' Returns the maxValue of an array '''
def maxVal(tab):
    width, height = tab.shape
    max = 0;
    for i in range(width):
        for j in range(height):
            max = tab[i][j] if tab[i][j] > max else max
    return max

#  cA (LL) |   cH (LH)
#---------------------
#  cV (HL) |   cD (HH)
# coeff => (cA, (cH,cV,cD) )
''' Reconstructs an image from the four coefficient matrix '''
def imageDWT(cRed,cGreen,cBlue):
    #Channel Red
    cARed = numpy.array(cRed[0])
    width,height = cARed.shape
    cHRed = numpy.array(cRed[1][0])
    cVRed = numpy.array(cRed[1][1])
    cDRed = numpy.array(cRed[1][2])
    #Channel Green
    cAGreen = numpy.array(cGreen[0])
    cHGreen = numpy.array(cGreen[1][0])
    cVGreen = numpy.array(cGreen[1][1])
    cDGreen = numpy.array(cGreen[1][2])
    #Channel Blue
    cABlue = numpy.array(cBlue[0])
    cHBlue = numpy.array(cBlue[1][0])
    cVBlue = numpy.array(cBlue[1][1])
    cDBlue = numpy.array(cBlue[1][2])    
    
    #We computing there the maxValue per channel par matrix
    cAMaxRed   = maxVal(cARed)
    cAMaxGreen = maxVal(cAGreen)
    cAMaxBlue  = maxVal(cABlue)

    cHMaxRed   = maxVal(cHRed)
    cHMaxGreen = maxVal(cHGreen)
    cHMaxBlue  = maxVal(cHBlue)
    
    cVMaxRed   = maxVal(cVRed)
    cVMaxGreen = maxVal(cVGreen)
    cVMaxBlue  = maxVal(cVBlue)

    cDMaxRed   = maxVal(cDRed)
    cDMaxGreen = maxVal(cDGreen)
    cDMaxBlue  = maxVal(cDBlue)
    
    dwt_img = Image.new("RGB",(width*2,height*2),(0,0,20))   
    #cA reconstruction
    for i in range(width):
        for j in range(height):
            R = cARed[i][j]
            R = (R/cAMaxRed)*160.0
            G = cAGreen[i][j]
            G = (G/cAMaxGreen)*85.0
            B = cABlue[i][j]
            B = (B/cAMaxBlue)*100.0
            dwt_img.putpixel((i,j) , (int(R),int(G),int(B)) )    
    #cH reconstruction
    for i in range(width):
        for j in range(height):
            R = cHRed[i][j]
            R = (R/cHMaxRed)*160.0
            G = cHGreen[i][j]
            G = (G/cHMaxGreen)*85.0
            B = cHBlue[i][j]
            B = (B/cHMaxBlue)*100.0
            dwt_img.putpixel((i+width,j) , (int(R),int(G),int(B)) )
    #cV reconstruction
    for i in range(width):
        for j in range(height):
            R = cVRed[i][j]
            R = (R/cVMaxRed)*160.0
            G = cVGreen[i][j]
            G = (G/cVMaxGreen)*85.0
            B = cVBlue[i][j]
            B = (B/cVMaxBlue)*100.0
            dwt_img.putpixel((i,j+height) , (int(R),int(G),int(B)) )
    #cD reconstruction
    for i in range(width):
        for j in range(height):
            R = cDRed[i][j]
            R = (R/cDMaxRed)*160.0
            G = cDGreen[i][j]
            G = (G/cDMaxGreen)*85.0
            B = cDBlue[i][j]
            B = (B/cDMaxBlue)*100.0
            dwt_img.putpixel((i+width,j+height) , (int(R),int(G),int(B)) )
    return dwt_img

''' Methode qui n'a pas l'air de fonctionner '''
def compareTwoImages(img0,img1):
    img0 = img0.convert('RGB')
    width, height = img0.size
    img1 = img1.convert('RGB')
    width1, height1 = img1.size
    nbDiff = 0
    for x in range(width):
        for y in range(height):
            r,g,b = img0.getpixel((x,y))
            r1,g1,b1 = img1.getpixel((x,y))
            nbDiff = nbDiff + 1 if (r != r1 or g != g1 or b != b1) else nbDiff
    return nbDiff

'''Main method that allows to compress an image by using DWT'''
def main(path):
    img0 = loadImg(path)
    img = loadImg(path)
    #img.save("DATA/1.jpg")
    width,height = img.size
    yuvImg = RGBtoYUV(img)
    yuvImg.save("DATA/2.jpg")
    #Gets the coefficients from each channel
    coR = pixelsRed(yuvImg)#There we're getting the coefficient of the red channel
    coG = pixelsGreen(yuvImg)#There we're getting the coefficient of the green channel
    coB = pixelsBlue(yuvImg)#There we're getting the coefficient of the blue channel
    dwt = imageDWT(coR,coG,coB)
    dwt.save("DATA/3.jpg")
    #quantification()
    idwt(coR,coG,coB, img)
    img.save("DATA/4.jpg")
    img = YUVtoRGB(img)
    img.save("DATA/5.jpg")


if __name__ == '__main__':
    main()