import src.dwt as dwt
#import windows

def run():
    pathImg = "DATA/"
    filename = "simon.png"
    pathImg = pathImg+filename
    print pathImg
    dwt.run()
    #windows.main(pathImg)

if __name__ == '__main__':
    run()
