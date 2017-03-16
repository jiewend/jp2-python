import dwt
import windows

def main():
    pathImg = "DATA/"
    filename = "simon.png"
    pathImg = pathImg+filename
    dwt.main(pathImg)
    windows.main(pathImg)

if __name__ == '__main__':
    main()
