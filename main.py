# -*- coding: utf-8 -*-
"""
Created on Tue May 30 01:20:22 2017

@author: VICTORMANUEL
"""
from Utileria import leerCadena
from Utileria import leerEntero
from Imagen import Imagen
from Imagenes import Imagenes
from listas import listaNom
from listas import listaRutas
from listas import listaImg
from listas import mostrar


def mainImg():
    ruta = "/home/victor/Imágenes/Imagenes/"
    listaRuta = listaRutas(ruta)
    listaNombre = listaNom(ruta)
    listaTodo = listaImg(ruta)
    imagenes = Imagenes()
    opciones = "1.-Etiquetar imagenes"
    opciones += "\n2.-Buscar Imagen"
    opciones += "\n3.-Buscar clase"
    opciones += "\n4.-Salir\n"
    clases = []
    salir = True
    while salir:
        res = leerEntero(opciones)
        
        
        if res == 1:
            i = 0
            while i < listaNombre:
                mostrar( listaTodo[i] )
                etiqueta = leerCadena("Digite la etiquete de la imagen " + listaNombre[i] + ":\n")
                clase = leerCadena("Digite la clase de la imagen " + listaNombre[i] + ":\n")
                if  not clase in clases:
                    clases.append(clase)
                img = Imagen(listaRuta[i], listaNombre[i], etiqueta , clase)
                imagenes.agregar(img)
                i += 1
                
                
        if res == 2:
            if imagenes.vacio():
                print "BIBLIOTECA VACIA"
            else: 
                mn = leerCadena("Digite la nombre de la imagen "  + ":\n")
                if imagenes.existe(mn):
                    imagenes[imagenes.buscar(mn)].mostrar()
                else: 
                    print "IMAGEN INEXISTENTE"
                
        if res == 3:
            if imagenes.vacio():
                print "BIBLIOTECA VACIA" 
            else:
                cl = leerCadena("Digite la clase a buscar " +  ":\n")
                if clase in clases:
                    for m in imagenes:
                        if m.getClase() == cl:
                            m.mostrar()
                            print m
        if res == 4:
            salir = False
        
            

    
        
mainImg()