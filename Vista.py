import Tkinter
from Modelo import WEtiqueta
from listas import listaNom, listaImg, listaRutas
from Imagen import Imagen
from Imagenes import Imagenes
from Imagen import Imagen
from Tkinter import Label, Entry
import tkMessageBox
from PIL import Image, ImageTk


imagenes =  Imagenes()
ruta = 'Comic'



def Main():
    root = Tkinter.Tk()
    boton = Tkinter.Button(root, text="Etiquetar", command= lambda: etiquetar(root))
    bt = Tkinter.Button(root, text="Busqueda", command= lambda: busqueda(root))
    boton.pack()
    bt.pack()
    root.mainloop()






def etiquetar(root):
    nombres = listaNom(ruta)
    ruNo = listaImg(ruta)
    rut = listaRutas(ruta)
    
    for i in range(len(nombres)):
        llen = True
        while llen:
            otra_ventana = Tkinter.Toplevel(root)
           
            
            otra_ventana=WEtiqueta(otra_ventana, ruNo[i] , nombres[i])
            
            otra_ventana.title("Etiquetado")
            siguiente = Tkinter.Button(otra_ventana, text="siguiente",command = lambda: sig(root), font = ('FreeSans', 14), cursor="hand1")
            cancel = Tkinter.Button(otra_ventana, text="Cancelar",command = lambda: can(root) , font = ('FreeSans', 14), cursor="hand1")
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
            etiqueta = ''
            clase = ''
            tex = 'Nombre: ' + nombres[i]
            l2 = Label(otra_ventana, text=tex, font = ('FreeSans', 14))
            l3 = Label(otra_ventana, text="Etiqueta", font = ('FreeSans', 14))
            e1 = Entry(otra_ventana, bd = 5, textvariable = etiqueta) 
            l4 = Label(otra_ventana, text="Categoria", font = ('FreeSans', 14))
            e2 = Entry(otra_ventana, bd = 5, textvariable = clase) 
        #Agregado
            l1.pack()
            l2.pack()
            l3.pack(side = 'left')
            e1.pack()
            l4.pack(side = 'left')
            e2.pack()
            siguiente.pack(side = 'right')
            cancel.pack()
            
            
            if clase != '' and etiqueta != '':
                Img = Imagen(rut[i], nombres[i], etiqueta, clase)
                imagenes.agregar(Img)
                llen = False
            else:
                tkMessageBox.FunctionName(title = 'ERROR', message = 'Campos vacios').pack()
            
            otra_ventana.mainloop()
            
               
        
        
def busqueda(root):
    otra_ventana = Tkinter.Toplevel(root)
    bus = ''
    entry = Entry(otra_ventana, bd = 5, textvariable = bus)
    entry.pack()
    otra_ventana.mainloop()
    
        
        
def sig(root):
    root.quit()
    root.destroy()
    
def can(root):
    root.destroy()
    
    
    



Main()