# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grap.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setStyleSheet('background-color:#D3D3D3')
        self.label.setText("")
        self.label.setObjectName("label")
        self.graph = QtWidgets.QLabel(Form)
        self.graph.setGeometry(QtCore.QRect(200, 10, 591, 531))
        self.graph.setText("")
        self.graph.setScaledContents(True)
        self.graph.setObjectName("graph")
        self.forward = QtWidgets.QPushButton(Form)
        self.forward.setGeometry(QtCore.QRect(40, 200, 113, 32))
        self.forward.setObjectName("forward")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(5, 270, 191, 31))
        self.label_3.setObjectName("label_3")
        self.time = QtWidgets.QComboBox(Form)
        self.time.setGeometry(QtCore.QRect(40, 410, 121, 26))
        self.time.setObjectName("time")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(9, 380, 181, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.val = QtWidgets.QLabel(Form)
        self.val.setGeometry(80, 335, 60, 22)
        self.val.setText('280 ppm')
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setText('Reset')
        self.reset.setGeometry(QtCore.QRect(40, 490, 113, 32))
        self.expo = QtWidgets.QPushButton(Form)
        self.expo.setText('Export as File')
        self.expo.setGeometry(QtCore.QRect(37, 530, 117, 32))
        self.note = QtWidgets.QLabel(Form)
        self.note.setGeometry(QtCore.QRect(300, 555, 500, 64))
        self.note.setStyleSheet('font-size:18pt')
        self.note.setText('Note : Equation mentioned in presentation slide-4')
        self.ppm = QtWidgets.QSlider(Form)
        self.ppm.setGeometry(QtCore.QRect(20, 310, 160, 22))
        self.ppm.setMinimum(280)
        self.ppm.setMaximum(1200)
        self.ppm.setSingleStep(20)
        self.ppm.setOrientation(QtCore.Qt.Horizontal)
        self.ppm.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ppm.setTickInterval(20)
        self.ppm.setObjectName("ppm")
        self.time.addItems(['2 years', '5 years', '10 years'])
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 177, 101))
        mov = QtGui.QMovie('mov.gif')
        self.label_2.setMovie(mov)
        mov.start()
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Graph 2"))
        self.forward.setText(_translate("Form", "Forward"))
        self.label_3.setText(_translate("Form", "Carbon Dioxide Concentration\n"
"                     in PPM"))
        self.label_4.setText(_translate("Form", "Time Step"))

