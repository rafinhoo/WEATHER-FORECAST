# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rafael\Desktop\PROJETINHO\LOGIN\tela1login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(535, 456)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(101, 252, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labeltext0 = QtWidgets.QLabel(self.centralwidget)
        self.labeltext0.setGeometry(QtCore.QRect(140, 10, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        self.labeltext0.setFont(font)
        self.labeltext0.setStyleSheet("background-color: rbg(255, 255, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;")
        self.labeltext0.setLineWidth(15)
        self.labeltext0.setMidLineWidth(15)
        self.labeltext0.setTextFormat(QtCore.Qt.MarkdownText)
        self.labeltext0.setIndent(7)
        self.labeltext0.setOpenExternalLinks(False)
        self.labeltext0.setObjectName("labeltext0")
        self.powerlabel = QtWidgets.QLabel(self.centralwidget)
        self.powerlabel.setGeometry(QtCore.QRect(10, 430, 131, 16))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        self.powerlabel.setFont(font)
        self.powerlabel.setObjectName("powerlabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(250, 216, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(250, 216, 255);\n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-radius: 15px; \n"
"border-color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rbg(255, 255, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 210, 251, 51))
        self.lineEdit_2.setStyleSheet("background-color: rbg(255, 255, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 420, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(250, 216, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(250, 216, 255);\n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-radius: 15px; \n"
"border-color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 47, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\rafael\\Desktop\\PROJETINHO\\LOGIN\\../../../Documents/PROJETO/LOGIN/icon email.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 220, 47, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\rafael\\Desktop\\PROJETINHO\\LOGIN\\../../../Documents/PROJETO/LOGIN/icon senha.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(250, 216, 255);\n"
"border-radius: 15px; \n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(250, 216, 255);\n"
"border-style: outset; \n"
"border-width: 2px;\n"
"border-radius: 15px; \n"
"border-color: white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 270, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ff0901")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela principal"))
        self.labeltext0.setText(_translate("MainWindow", "WEATHER FORECAST"))
        self.powerlabel.setText(_translate("MainWindow", "POWERED BY: RAFAEL"))
        self.pushButton.setText(_translate("MainWindow", "CONFIRMAR"))
        self.label.setText(_translate("MainWindow", "Não é cadastrado?"))
        self.pushButton_2.setText(_translate("MainWindow", "CADASTRAR"))
        self.pushButton_3.setText(_translate("MainWindow", "SAIR"))