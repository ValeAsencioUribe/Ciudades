# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui

class Ui_Ventana(object):

    def setupUi(self, Formu2):
        Formu2.setObjectName("Formu2")
        Formu2.resize(400,600)
        
        self.label = QtGui.QLabel(Formu2)
        self.label.setGeometry(QtCore.QRect(30,15,300, 16))
        self.label.setObjectName("label")
        #paises
        self.label1 = QtGui.QLabel(Formu2)
        self.label1.setGeometry(QtCore.QRect(130,45,300, 16))
        self.label1.setObjectName("label")
        self.combo_paises = QtGui.QComboBox(Formu2)
        self.combo_paises.setGeometry(QtCore.QRect(100,70, 140, 25))
        self.combo_paises.setObjectName("combo_marca ")
        #nombre ciudad
        self.label2 = QtGui.QLabel(Formu2)
        self.label2.setGeometry(QtCore.QRect(110,110,300, 16))
        self.label2.setObjectName("label")
        self.search_box = QtGui.QLineEdit(Formu2)
        self.search_box.setGeometry(QtCore.QRect(80, 130, 200, 25))
        self.search_box.setObjectName("search_box")
        #Poblacion
        self.label3 = QtGui.QLabel(Formu2)
        self.label3.setGeometry(QtCore.QRect(110,170,300, 16))
        self.label3.setObjectName("label")
        self.search_box1 = QtGui.QLineEdit(Formu2)
        self.search_box1.setGeometry(QtCore.QRect(80, 190, 200, 25))
        self.search_box1.setObjectName("search_box1")
        #fundacion
        self.label4 = QtGui.QLabel(Formu2)
        self.label4.setGeometry(QtCore.QRect(110,230,300, 16))
        self.label4.setObjectName("label")
        self.search_box2 = QtGui.QLineEdit(Formu2)
        self.search_box2.setGeometry(QtCore.QRect(80, 250, 200, 25))
        self.search_box2.setObjectName("search_box2")
        #superficie
        self.label5 = QtGui.QLabel(Formu2)
        self.label5.setGeometry(QtCore.QRect(110,290,300, 16))
        self.label5.setObjectName("label")
        self.search_box3 = QtGui.QLineEdit(Formu2)
        self.search_box3.setGeometry(QtCore.QRect(80, 310, 200, 25))
        self.search_box3.setObjectName("search_box3")
        #densidad
        self.label6 = QtGui.QLabel(Formu2)
        self.label6.setGeometry(QtCore.QRect(110,350,300, 16))
        self.label6.setObjectName("label")
        self.search_box4 = QtGui.QLineEdit(Formu2)
        self.search_box4.setGeometry(QtCore.QRect(80, 370, 200, 25))
        self.search_box4.setObjectName("search_box4")
        #gentilicio
        self.label7 = QtGui.QLabel(Formu2)
        self.label7.setGeometry(QtCore.QRect(110,410,300, 16))
        self.label7.setObjectName("label")
        self.search_box5 = QtGui.QLineEdit(Formu2)
        self.search_box5.setGeometry(QtCore.QRect(80, 430, 200, 25))
        self.search_box5.setObjectName("search_box5")
        
        #guardar
        self.button1= QtGui.QPushButton(Formu2)
        self.button1.setGeometry(QtCore.QRect(60,500,100,25))
        self.button1.setObjectName("button1")
        #salir
        self.button2= QtGui.QPushButton(Formu2)
        self.button2.setGeometry(QtCore.QRect(200,500,100,25))
        self.button2.setObjectName("button2")

        self.retranslateUi(Formu2)
        QtCore.QMetaObject.connectSlotsByName(Formu2)
        
    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "Ventana", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Formu2", "Formulario de ingreso", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("Formu2", "Paises", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Formu2", "Nombre de la ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Formu2", "Poblacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("Formu2", "Fecha de Fundacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("Formu2", "Superficie", None, QtGui.QApplication.UnicodeUTF8))
        self.label6.setText(QtGui.QApplication.translate("Formu2", "Densidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("Formu2", "Gentilicio", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese el nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box1.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese poblacion", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box2.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese fundacion", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box3.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese superficie", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box4.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese densidad", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box5.setPlaceholderText(QtGui.QApplication.translate("Formu2", "Ingrese gentilicio", None, QtGui.QApplication.UnicodeUTF8))
        self.button1.setText(QtGui.QApplication.translate("Formu2", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.button2.setText(QtGui.QApplication.translate("Formu2", "Salir", None, QtGui.QApplication.UnicodeUTF8))
