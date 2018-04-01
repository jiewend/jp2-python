'Main Module'
#!/usr/bin/python
import os
import src.utils as util
import src.compression as dwt
import src.windows as win
import numpy as np

def run():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    print (util.max_ndarray(x))

if __name__ == '__main__':
    run()
