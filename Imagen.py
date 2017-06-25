"""
Created on Tue May 23 23:56:33 2017

@author: VICTORMANUEL
"""
import matplotlib.pyplot as plt

class Imagen:
# -*- coding: utf-8 -*-
    def __init__(self, ruta, nombre, etiqueta, clase):
        self.ruta = ruta
        self.nombre = nombre 
        self.etiqueta = etiqueta
        self.clase = clase
        self.Id = None
        
    def __str__(self):
       return "Ruta: " + self.ruta + "\nNombre: " +  self.nombre + "\nEtiqueta: " + self.etiqueta + "\nClase: " + self.clase + "\nId: " + self.Id 
    
    def setRuta(self, ruta):
        self.ruta = ruta
        
    def getRuta(self):
        return self.ruta
    
    def setNombre(self, nombre):
        self.nombre = nombre 
        
    def getNombre(self):
        return self.nombre
    
    def setEtiqueta(self, etiqueta):
        self.etiqueta = etiqueta
        
    def getEtiqueta(self):
        return self.etiqueta
    
    def setID(self, Id):
        self.Id = Id
        
    def getID(self):
        return self.categoria
    
    def setClase(self, clase):
        self.clase = clase
           
    def getClase(self):
        return self.clase
       
    #def mostrar(self):
        #try:
            #img = mpimg.imread(self.getRuta + self.getNombre)
            #plt.imshow(img)
        #except: 
         # print "EERROR DE ARCHIVO"
          
    def Json(self):
        if self.getID == None:
            return '{\n"ruta": ' + '"' + self.getRuta() + '",' + '\n"nombre": ' + '"' + self.getNombre() + '",' + '\n"etiqueta": ' + '",' + self.getEtiqueta() + '",' + '\n"clase": ' + '"' + self.getClase() + '",' + '\n"id": ' + '"' + self.Id + '"\n}' 
        else:
            return '{\n"ruta": ' + '"' + self.getRuta() + '",' + '\n"nombre": ' + '"' + self.getNombre() + '",' + '\n"etiqueta": ' + '",' + self.getEtiqueta() + '",' + '\n"clase": ' + '"' + self.getClase() + '",' + '\n"id": ' + '"None"\n}' 
    