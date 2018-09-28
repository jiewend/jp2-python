import pywt
import numpy as np

def test1(arr):
    aa1 =[1,2, 3, 4]
    aa1dwt = pywt.dwt(aa1, 'haar')
    aa1re = pywt.idwt(aa1dwt[0], aa1dwt[1], 'haar')
    print aa1
    print aa1dwt
    print aa1re

def test2(arr):
    aa2 = [[1, 2, 3, 4], [2, 3, 4, 5]]
    aa2dwt = pywt.dwt2(aa2, 'haar')
    aa20re = pywt.idwt(aa2dwt[0], aa2dwt[1][0], 'haar')
    aa21re = pywt.idwt(aa2dwt[0], aa2dwt[1][1], 'haar')
    aa22re = pywt.idwt(aa2dwt[0], aa2dwt[1][2], 'haar')

    aa2dwt0 = np.concatenate((aa2dwt[0], aa2dwt[1][1]), axis=0)
    aa2dwt1 = np.concatenate((aa2dwt[1][0], aa2dwt[1][2]), axis=0)
    print aa2dwt
    print 
    print aa2dwt0, aa2dwt1

    bb0 = pywt.idwt(aa2dwt0, aa2dwt1, 'haar')
    bb = pywt.idwt(bb0[:, 0:2], bb0[:, 2:], 'haar')
    print 
    print bb0[:, 0:2]
    print bb0[:, 2:]

    print
    print bb0
    print bb


    



if __name__ == '__main__':
    # test(1)
    test2(1)

