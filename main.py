import src.dwt as dwt
import src.windows as win

def run():
    pathImg = 'DATA/'
    filename = 'lena.png'
    pathImg = pathImg+filename
    print pathImg
    dwt.run(pathImg)
    win.run(pathImg)

if __name__ == '__main__':
    run()
