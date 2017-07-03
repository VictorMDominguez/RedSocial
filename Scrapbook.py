from PIL import Image, ImageTk
#from Imagen import Imagen
from Tkinter import Label, Frame, Button, Tk, PhotoImage
import os
from listas import listaNom, listaImg, listaRutas

class Scrapbook:
   
    
    def __init__(self, master=None):
        self.master = master
        self.frame = Frame(master, width=700, height=520, bg='gray50', relief='raised', bd=4)
        self.images = listaImg('Comic')
        images = os.listdir("Comic")
        self.lbl = Label(self.frame)
        self.lbl.place(relx=0.5, rely=0.48, anchor='center')
        xpos = 0.05
        for i in range(15):
            #, anchor=S
            photo=PhotoImage(file = '1.gif')
            b = Button(self.frame, text='%d'%(i+1) , fg='white', command=lambda s=self, img=i: s.getImg(img))
            b.config(image = photo,width = "10",height = "10")
            b.place(relx=xpos, rely=0.9)
            self.images.append(images[i])
            xpos = xpos + 0.08
        # , anchor=SE
        Button(self.frame, text='Done', command=self.exit, bg='red', fg='yellow').place(relx=0.99, rely=0.99 )
        self.frame.pack()
        self.getImg(0)
        
    def getImg(self, img):
        self.masterImg = Image.open(os.path.join("images", self.images[img]))
        
        self.masterImg.thumbnail((400, 400))
        self.img = ImageTk.PhotoImage(self.masterImg)
        self.lbl['image'] = self.img
    
    def exit(self):
        self.master.destroy()

root = Tk()
root.title('Scrapbook')
scrapbook = Scrapbook(root)
root.mainloop()