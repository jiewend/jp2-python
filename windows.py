import Tkinter as tk
from PIL import Image, ImageTk

def main(path):
    # This creates the main window for application
    window = tk.Tk()
    # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img0 = ImageTk.PhotoImage(Image.open(path))
    # This creates the main window of an application
    window.title("Wavelet compression")
    window.geometry(str(5*img0.width())+"x"+str(img0.height()))
    window.configure(background='grey')

    img1 = ImageTk.PhotoImage(Image.open("DATA/2.jpg"))
    img2 = ImageTk.PhotoImage(Image.open("DATA/3.jpg"))
    img3 = ImageTk.PhotoImage(Image.open("DATA/4.jpg"))
    img4 = ImageTk.PhotoImage(Image.open("DATA/5.jpg"))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel1 = tk.Label(window, image = img0)#Original
    panel2 = tk.Label(window, image = img1)#YCbCr
    panel3 = tk.Label(window, image = img2)#DWT
    panel4 = tk.Label(window, image = img3)#iDWT YCbCr
    panel5 = tk.Label(window, image = img4)#iDWT RGB

    #The Pack geometry manager packs widgets in rows or columns.
    panel1.pack(side = "left", fill = "both", expand = "yes")
    panel2.pack(side = "left", fill = "both", expand = "yes")
    panel3.pack(side = "left", fill = "both", expand = "yes")
    panel4.pack(side = "left", fill = "both", expand = "yes")
    panel5.pack(side = "left", fill = "both", expand = "yes")

    #Start the GUI
    window.mainloop()

if __name__ == '__main__':
    main()
