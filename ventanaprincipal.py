# -*- coding: utf-8 -*-
import controller

from PySide import QtCore, QtGui

class Ui_Ventana(object):

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        #Creamos las dimensiones de la grilla
        self.table_categoria= QtGui.QTableView(Window)
        self.table_categoria.setGeometry(QtCore.QRect(60,90,920,500))
        self.table_categoria.setObjectName("table_producto")
        self.table_categoria.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_categoria.setAlternatingRowColors(True)
        self.table_categoria.setSortingEnabled(True)
        #caja de texto para buscar ciudades
        self.search_box = QtGui.QLineEdit(Window)
        self.search_box.setGeometry(QtCore.QRect(80, 50, 210, 25))
        #boton para buscar
        self.search_box.setObjectName("search_box")
        self.button1= QtGui.QPushButton(Window)
        self.button1.setGeometry(QtCore.QRect(300,50,100,25))
        self.button1.setObjectName("button1")
        #boton para agregar
        self.button2= QtGui.QPushButton(Window)
        self.button2.setGeometry(QtCore.QRect(500,50,100,25))
        self.button2.setObjectName("button2")
        #boton para editar
        self.button3= QtGui.QPushButton(Window)
        self.button3.setGeometry(QtCore.QRect(610,50,100,25))
        self.button3.setObjectName("button3")
        #boton para eliminar
        self.button4= QtGui.QPushButton(Window)
        self.button4.setGeometry(QtCore.QRect(720,50,100,25))
        self.button4.setObjectName("button4")
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        
    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Ventana", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("Window", "Buscar ciudades", None, QtGui.QApplication.UnicodeUTF8))
        self.button1.setText(QtGui.QApplication.translate("Window", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.button2.setText(QtGui.QApplication.translate("Window", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.button3.setText(QtGui.QApplication.translate("Window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.button4.setText(QtGui.QApplication.translate("Window", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
