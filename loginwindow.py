# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import DB_operation
import tkinter
import tkinter.messagebox
import _winapi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("金贝教育")
        MainWindow.resize(588, 417)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_login = QtWidgets.QPushButton(self.centralwidget)
        self.bt_login.setGeometry(QtCore.QRect(230, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bt_login.setFont(font)
        self.bt_login.setObjectName("bt_login")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 201, 21))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 160, 201, 21))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(130, 120, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(150, 160, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.bt_login.clicked.connect(self.btu_even)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_login.setText(_translate("MainWindow", "登 录"))
        self.label_ID.setText(_translate("MainWindow", "用户名："))
        self.label_password.setText(_translate("MainWindow", "密码："))

    def btu_even(self):
        id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        result = DB_operation.login(id, password)
        return result
