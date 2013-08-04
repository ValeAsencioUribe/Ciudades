#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller
import ventana
import ventana1

from PySide import QtGui, QtCore
from ventanaprincipal import Ui_Ventana

class main(QtGui.QWidget):

    def __init__(self):#funcion para definir los metodos que ocuparemos
        super(main, self).__init__()
        self.ui = Ui_Ventana()
        self.ui.setupUi(self)
        self.cargar_categoria()
        self.show()
	self.set_signals()
	    
    def cargar_categoria(self, ciudades=None, paises=None): #funcion para cargar la bd en la grilla
        if ciudades is None:
            ciudades = controller.get_ciudades()#obtenemos las ciudades
            paises = controller.get_paises()#obtenemos las recetas
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(ciudades),7)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Pais"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Poblacion (hab)"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Fundacion"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Superficie (km²)"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Densidad (hab/km²)"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Gentilicio"))    
        self.ui.table_categoria.setModel(self.model)
        self.ui.table_categoria.setColumnWidth(0,125)
        self.ui.table_categoria.setColumnWidth(1,130)
        self.ui.table_categoria.setColumnWidth(2,120)
        self.ui.table_categoria.setColumnWidth(3,120)
        self.ui.table_categoria.setColumnWidth(4,115)
        self.ui.table_categoria.setColumnWidth(5,140)
        self.ui.table_categoria.setColumnWidth(6,125)
        
        i = 0
        for row in paises:#recorremos los paises y mostramos el nombre
            index = self.model.index(i, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['Nombre'])
            i = i+1
            
        r = 0
        for row in ciudades:#recorremos las ciudades y mostramos los atributos en la grilla
	    index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['poblacion'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['fundacion'])
            index = self.model.index(r, 4, QtCore.QModelIndex()); 
            self.model.setData(index, row['superficie'])
            index = self.model.index(r, 5, QtCore.QModelIndex()); 
            self.model.setData(index, row['densidad'])
            index = self.model.index(r, 6, QtCore.QModelIndex()); 
            self.model.setData(index, row['gentilicio'])
            r = r+1
            
    def set_signals(self):
        self.ui.button4.clicked.connect(self.delete)
        self.ui.button2.clicked.connect(self.v_formulario)
        self.ui.button3.clicked.connect(self.e_formulario)
        
    def v_formulario(self):
	formu = ventana.Formu(self)
	
    def e_formulario(self):
        formu = ventana1.Formu2(self)
            
    def delete(self):
        model = self.ui.table_categoria.model()
        index = self.ui.table_categoria.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
	    codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(codigo)):
                self.cargar_categoria()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("La ciudad fue eliminada.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False	
def run():
    app = QtGui.QApplication(sys.argv)
    ma = main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
        
            
