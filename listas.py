# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:38:02 2017

@author: VICTORMANUEL
"""
from os import walk
import os.path
import numpy
import matplotlib.pyplot  as plt
import matplotlib.image as mpimg

import os
from os import walk
from PIL import Image
from Imagen import *


def diccionario(ruta):
    imagenes = {}
    for (ruta,carpeta,imagen) in walk(ruta):
        imagenes[ruta] = imagen
    return imagenes

            
def listaImg(ruta):
    imagenes = diccionario(ruta)
    lista = []
    for ce in imagenes:
        for me in imagenes[ce]:
            if me.endswith(('.png', '.jpg', '.gif')):
                lista.append( ce + "/" + me )
    return lista


            
def listaNom(ruta):
    imagenes = diccionario(ruta)
    lista = []
    for ce in imagenes:
        for me in imagenes[ce]:
            if me.endswith(('.png', '.jpg', '.gif')):
                lista.append( me )
    return lista



def listaRutas(ruta):
    imagenes = diccionario(ruta)
    lista = []
    for ce in imagenes:
        for me in imagenes[ce]:
            if me.endswith(('.png', '.jpg', '.gif')):
                lista.append( ce )
    return lista



def mostrar(ruta):
    try:
        img = mpimg.imread(ruta)
        plt.imshow(img)
    except: 
          print "Error de archivo"
    return "hola" 
    

