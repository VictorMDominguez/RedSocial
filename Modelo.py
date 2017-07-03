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


ruta = '/home/plagueis/Imágenes/Comic'

#listas
nombres = listaNom(ruta)
rutas = listaRutas(ruta)
ruNo = listaImg(ruta)

    
#Botones
    

def no():
    for i in range(len(nombres)):
    
        
        top = Tkinter.Tk()
        top.title("Imagenes")
        siguiente = Tkinter.Button(top, text="siguiente",command = top.destroy, font = ('FreeSans', 14), cursor="hand1")
        cancel = Tkinter.Button(top, text="Cancelar",command = None , font = ('FreeSans', 14), cursor="hand1")
        #top.
    #Imagen
        image = Image.open(ruNo[i])
        if image.height > 1200 or image.width > 1200:
            image.thumbnail((image.height / 4 ,image.width / 4))
        
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
        l4 = Label(top, text="Categoria", font = ('FreeSans', 14))
        e2 = Entry(top, bd = 5) 
    #Scroll
        #scrollbar = Scrollbar(top)
        #scrollbar.pack( side = 'right', fill='y' )
    
    #Agregado
        l1.pack()
        l2.pack()
        l3.pack(side = 'left')
        e1.pack()
        l4.pack(side = 'left')
        e2.pack()
        siguiente.pack(side = 'right')
        top.mainloop()
    
    
def sig(root):
    root.quit()
    root.destroy()
    
def can(root):
    root.destroy()
    
    
def WEtiqueta(root, ruta, nombre):
    root.title("Etiquetado")
    siguiente = Tkinter.Button(root, text="siguiente",command = lambda: sig(root), font = ('FreeSans', 14), cursor="hand1")
    cancel = Tkinter.Button(root, text="Cancelar",command = lambda: can(root) , font = ('FreeSans', 14), cursor="hand1")
    #top.
#Imagen
    image = Image.open(ruta)
    if image.height > 1200 or image.width > 1200:
        image.thumbnail((image.height / 4 ,image.width / 4))
    
    if image.height > 800 or image.width > 800:
        image.thumbnail((image.height / 2 ,image.width / 2))
    
    photo = ImageTk.PhotoImage(image)
    l1 = Label(root,image=photo, justify = 'center')
    l1.image = photo
#Texto
    tex = 'Nombre: ' + nombre 
    l2 = Label(root, text=tex, font = ('FreeSans', 14))
    l3 = Label(root, text="Etiqueta", font = ('FreeSans', 14))
    e1 = Entry(root, bd = 5) 
    l4 = Label(root, text="Categoria", font = ('FreeSans', 14))
    e2 = Entry(root, bd = 5) 


#Agregado
    l1.pack()
    l2.pack()
    l3.pack(side = 'left')
    e1.pack()
    l4.pack(side = 'left')
    e2.pack()
    siguiente.pack(side = 'right')
    cancel.pack()
    return root