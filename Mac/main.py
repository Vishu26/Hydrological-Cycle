from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(864, 660)
        self.back = QtWidgets.QLabel(Form)
        self.back.setGeometry(0, 0, 864, 640)
        self.back.setScaledContents(True)
        self.back.setPixmap(QtGui.QPixmap('water.jpg'))
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 560, 871, 99))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet('font-size:18pt')
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 0, 641, 561))
        self.label.setText("")
        op = QtGui.QMovie('water-cycle-anim.gif')
        self.label.setMovie(op)
        op.startTimer(10)
        op.start()
        QtCore.QTimer.singleShot(15000, lambda:self.done(Form))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.solar = QtWidgets.QPushButton(Form)
        self.solar.setGeometry(QtCore.QRect(750, 0, 113, 91))
        self.solar.setIcon(QtGui.QIcon('sun.png'))
        self.solar.setIconSize(QtCore.QSize(64, 64))
        self.solar.setObjectName("solar")
        self.cloud = QtWidgets.QPushButton(Form)
        self.cloud.setGeometry(QtCore.QRect(750, 110, 113, 91))
        self.cloud.setIcon(QtGui.QIcon('cloud.png'))
        self.cloud.setIconSize(QtCore.QSize(64, 64))
        self.cloud.setObjectName("cloud")
        self.rainfall = QtWidgets.QPushButton(Form)
        self.rainfall.setGeometry(QtCore.QRect(750, 220, 113, 91))
        self.rainfall.setIcon(QtGui.QIcon('rain.png'))
        self.rainfall.setIconSize(QtCore.QSize(64, 64))
        self.rainfall.setObjectName("rainfall")
        self.nitrogen = QtWidgets.QPushButton(Form)
        self.nitrogen.setGeometry(QtCore.QRect(750, 330, 113, 91))
        self.nitrogen.setIcon(QtGui.QIcon('n2.png'))
        self.nitrogen.setIconSize(QtCore.QSize(64, 64))
        self.nitrogen.setObjectName("nitrogen")
        self.removeplants = QtWidgets.QPushButton(Form)
        self.removeplants.setGeometry(QtCore.QRect(0, 0, 113, 91))
        self.removeplants.setIcon(QtGui.QIcon('plant.png'))
        self.removeplants.setIconSize(QtCore.QSize(64, 64))
        self.removeplants.setObjectName("removeplants")
        self.carbon = QtWidgets.QPushButton(Form)
        self.carbon.setGeometry(QtCore.QRect(0, 110, 113, 91))
        self.carbon.setIcon(QtGui.QIcon('co2.png'))
        self.carbon.setIconSize(QtCore.QSize(64, 64))
        self.carbon.setObjectName("carbon")
        self.oxygen = QtWidgets.QPushButton(Form)
        self.oxygen.setIcon(QtGui.QIcon('read.png'))
        self.oxygen.setIconSize(QtCore.QSize(64, 64))
        self.oxygen.setGeometry(QtCore.QRect(0, 220, 113, 91))
        self.oxygen.setObjectName("oxygen")
        self.sulphate = QtWidgets.QPushButton(Form)
        self.sulphate.setIcon(QtGui.QIcon('so2.png'))
        self.sulphate.setIconSize(QtCore.QSize(64, 64))
        self.sulphate.setGeometry(QtCore.QRect(0, 330, 113, 91))
        self.sulphate.setObjectName("sulphate")
        self.s1 = QtWidgets.QSlider(Form)
        self.s1.setGeometry(QtCore.QRect(590, 30, 160, 22))
        self.s1.setMaximum(3)
        self.s1.setSliderPosition(2)
        self.s1.setOrientation(QtCore.Qt.Horizontal)
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QSlider(Form)
        self.s2.setGeometry(QtCore.QRect(590, 140, 160, 22))
        self.s2.setMaximum(1)
        self.s2.setOrientation(QtCore.Qt.Horizontal)
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QSlider(Form)
        self.s3.setGeometry(QtCore.QRect(590, 250, 160, 22))
        self.s3.setMaximum(2)
        self.s3.setSliderPosition(1)
        self.s3.setOrientation(QtCore.Qt.Horizontal)
        self.s3.setObjectName("s3")
        self.s4 = QtWidgets.QSlider(Form)
        self.s4.setGeometry(QtCore.QRect(590, 360, 160, 22))
        self.s4.setMaximum(2)
        self.s4.setSliderPosition(1)
        self.s4.setOrientation(QtCore.Qt.Horizontal)
        self.s4.setObjectName("s4")
        self.s5 = QtWidgets.QSlider(Form)
        self.s5.setGeometry(QtCore.QRect(110, 30, 160, 22))
        self.s5.setMaximum(1)
        self.s5.setOrientation(QtCore.Qt.Horizontal)
        self.s5.setObjectName("s5")
        self.s6 = QtWidgets.QSlider(Form)
        self.s6.setGeometry(QtCore.QRect(110, 140, 160, 22))
        self.s6.setMaximum(1)
        self.s6.setSliderPosition(0)
        self.s6.setOrientation(QtCore.Qt.Horizontal)
        self.s6.setObjectName("s6")
        self.s8 = QtWidgets.QSlider(Form)
        self.s8.setGeometry(QtCore.QRect(110, 360, 160, 22))
        self.s8.setMaximum(1)
        self.s8.setSliderPosition(0)
        self.s8.setOrientation(QtCore.Qt.Horizontal)
        self.s8.setObjectName("s8")

        self.solar.setToolTip('Click Me!')
        self.oxygen.setToolTip('Click Me!')
        self.nitrogen.setToolTip('Click Me!')
        self.carbon.setToolTip('Click Me!')
        self.sulphate.setToolTip('Click Me!')
        self.removeplants.setToolTip('Click Me!')
        self.cloud.setToolTip('Click Me!')
        self.rainfall.setToolTip('Click Me!')
        self.solar.setToolTip('Click Me!')

        self.s1.hide()
        self.s2.hide()
        self.s3.hide()
        self.s4.hide()
        self.s5.hide()
        self.s6.hide()
        self.s8.hide()

        self.gra = QtWidgets.QPushButton(Form)
        self.gra.setGeometry(QtCore.QRect(0, 440, 113, 91))
        self.gra.setIcon(QtGui.QIcon('graph.png'))
        self.gra.setIconSize(QtCore.QSize(64, 64))

        self.gra2 = QtWidgets.QPushButton(Form)
        self.gra2.setGeometry(QtCore.QRect(750, 440, 113, 91))
        self.gra2.setIcon(QtGui.QIcon('gra2.png'))
        self.gra2.setIconSize(QtCore.QSize(64, 64))

        self.gra.setToolTip('Click Me!')
        self.gra2.setToolTip('Click Me!')

    def done(self, Form):
        self.label.setPixmap(QtGui.QPixmap("base1.jpg"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Water Cycle"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">This is the ideal case where every parameter of the cycle is normal/average.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">This ecosystem receives normal rainfall, normal solar energy and has ideal sea and ground water level.</span></p></body></html>"))

