# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:08:08 2017

@author: VICTORMANUEL
"""

from listas import listaNom, listaImg, listaRutas
from Imagen import Imagen
from Tkinter import Label, Entry
import Tkinter
from PIL import Image, ImageTk
import os
top = Tkinter.Tk()
top.title("Imagenes")

ruta = '/home/plagueis/Imágenes/Comic'

#listas
nombres = listaNom(ruta)
rutas = listaRutas(ruta)
ruNo = listaImg(ruta)



def sal():
    top.option_clear()
    
#Botones
siguiente = Tkinter.Button(top, text="siguiente",command = sal() , font = ('FreeSans', 14), cursor="hand1")


for i in range(len(nombres)):
    
#Imagen
    image = Image.open(ruNo[i])
    if image.height > 800 or image.width > 800:
        image.thumbnail((image.height / 2 ,image.width / 2))
    photo = ImageTk.PhotoImage(image)
    l1 = Label(image=photo, justify = 'center')
    l1.image = photo
#Texto
    tex = 'Nombre: ' + nombres[i] 
    l2 = Label(top, text=tex, font = ('FreeSans', 14))
    l3 = Label(top, text="Etiqueta", font = ('FreeSans', 14))
    e1 = Entry(top, bd = 5) 
#Agregado
    l1.pack()
    l2.pack()
    l3.pack(side = 'left')
    e1.pack()
    siguiente.pack(side = 'right')
    top.mainloop()
    
    
