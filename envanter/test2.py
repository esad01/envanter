__author__ = 'mek'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Databases", "Marka Eklendi  :")

B = Tkinter.Button(top, text ="EKLE", command = helloCallBack)

B.pack()
top.mainloop()