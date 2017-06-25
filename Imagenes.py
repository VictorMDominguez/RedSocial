# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:23:52 2017

@author: VICTORMANUEL
"""
class Imagenes():
    def __init__(self):
         self.lista = []
         
         
    def agregar(self, imagen):
        imagen.setID(int(len(self.lista)+1))
        self.lista.append(imagen)
        
    def existe(self, nombre ):
        i = 0
        resp = False
        while i < len(self.lista) and not resp:
            if self.lista[i].getNombre == nombre:
                resp = True
            i += 1
        return resp
    
    def buscar(self, nombre):
        i = 0
        resp = False
        while i < len(self.lista) and not resp:
            if self.lista[i].getNombre == nombre:
                resp = True
            i += 1
        return i
    
    def vacio(self):
        return self.lista == []
    
    def Json(self):
        resp = '{\n"Imagenes": {\n"Imagen": [
        for i in self.lista:
            resp += '\n' + i.Json()
        return resp + ']\n}\n}'