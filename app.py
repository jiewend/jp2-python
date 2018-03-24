'Main Module'
#!/usr/bin/python
import os
import src.utils as util
import src.dwt as dwt
import src.windows as win

def run():
    folder = 'data'
    filename = 'lenadd.png'
    img = util.loadImg(os.path.join(folder, filename))

if __name__ == '__main__':
    run()
