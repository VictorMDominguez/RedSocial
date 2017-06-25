#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 09:23:54 2017

@author: victor
"""

import Tkinter
top = Tkinter.Tk()

var = StringVar()
var.set("Hey!? How are you doing?")
label = Message( root, textvariable=var, relief=RAISED )


top.mainloop()