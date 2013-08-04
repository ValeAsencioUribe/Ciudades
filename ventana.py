#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from formulario import Ui_Ventana

class Formu(QtGui.QDialog):
	
    def __init__(self,parent=None, id_categoria=None, id_paises=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Ventana()
        self.ui.setupUi(self)
        self.show()
        self.cargar_paises()

    def cargar_paises(self):
        paises = controller.obtener_paises()
        self.ui.combo_paises.addItem("Todos", -1)
	for pais in paises:
	    self.ui.combo_paises.addItem(pais["nombre"], pais["id_pais"])
	#self.ui.combo_paises.activated[str].connect(self.datos) 
            
def run():
    app = QtGui.QApplication(sys.argv)
    ma = main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
