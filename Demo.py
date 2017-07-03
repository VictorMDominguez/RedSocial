from PIL import Image, ImageTk
#from Imagen import Imagen
from Tkinter import Label, Frame, Button, Tk
import os
from listas import listaNom, listaImg, listaRutas
class Scrapbook:
   
    
    def __init__(self, master=None):
        self.master = master
        self.frame = Frame(master, width=400, height=420, bg='gray50', relief='RAISED', bd=4)
        self.lbl = Label(self.frame)
        self.lbl.place(relx=0.5, rely=0.48, anchor='center')
        self.images = listaImg('/home/plagueis/imagenes/Comic')
        images = os.listdir("images")
        xpos = 0.05
        for i in range(10):
            #, anchor=S
            Button(self.frame, text='%d'%(i+1), bg='gray10', fg='white', command=lambda s=self, img=i: s.getImg(img)).place(relx=xpos, rely=0.99)
            xpos = xpos + 0.08
            self.images.append(images[i])
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

    