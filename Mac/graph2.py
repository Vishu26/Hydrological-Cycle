from grap2 import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.QtWidgets import *
import matplotlib as mpl

mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

class mas2(QWidget, Ui_Form):

    def __init__(self):

        super(mas2, self).__init__()
        self.setupUi(self)
        self.step = 2
        self.seax = [1990]
        self.seay = [30]
        self.cy = [0]
        self.conc = 0
        self.usage = 0.2
        self.lo = 0.02
        self.ppm.valueChanged.connect(self.se)
        self.forward.clicked.connect(self.go)
        self.time.currentIndexChanged.connect(self.t)
        self.use.currentIndexChanged.connect(self.u)
        self.loss.currentIndexChanged.connect(self.l)
        self.reset.clicked.connect(self.re)
        self.expo.clicked.connect(self.exp)


        fig, self.ax1 = plt.subplots()
        self.ax1.plot(self.seax, self.seay, '*', color='r')
        self.ax1.axis([1980, 2110, 15, 40])
        self.ax1.xaxis.grid()
        self.ax1.yaxis.grid()
        self.ax1.set_facecolor('gray')
        self.ax1.set_ylabel('Ground Water Level (in metres)')
        self.ax1.yaxis.label.set_color('red')
        self.ax1.tick_params(axis='y', colors='red')

        self.ax2 = self.ax1.twinx()
        self.ax2.plot(self.seax, self.cy, '^', color='b')
        self.ax2.axis([1980, 2110, 0, 2800])
        self.ax2.xaxis.grid()
        self.ax2.set_ylabel('Rainfall (in mm)')
        self.ax2.yaxis.label.set_color('blue')
        self.ax2.tick_params(axis='y', colors='blue')

        self.ax1.set_xlabel('Date (Year)')

        plt.savefig('fig.png')
        self.graph.setPixmap(QPixmap('fig.png'))
        self.show()

    def u(self):
        self.usage = float(self.use.currentText().split()[0])

    def l(self):
        self.lo = float(self.loss.currentText().split()[0])

    def exp(self):
        with open('graph.txt', 'w') as f:
            f.write('Date, Rainfall, Water\n')
            for i in range(len(self.cy)):
                f.write(str(self.seax[i])+', '+str(self.cy[i])+', '+str(self.seay[i])+'\n')
    def t(self):
        self.step = int(self.time.currentText().split()[0])
    def re(self):
        self.hide()
        self.__init__()


    def se(self):
        self.conc = self.ppm.value()
        self.val.setText(str(self.conc)+' mm')

    def go(self):
        self.cy.append(self.conc*10)
        self.seax.append(self.seax[-1] + self.step)
        if self.seax[-1] >= 2110:
            self.forward.setDisabled(True)
            return
        x = 25*np.log(self.conc + 1) + 20

        self.seay.append(((self.seay[-1]+x/1000)*(100-self.usage)/100)*(100-self.lo)/100)

        self.ax1.plot(self.seax, self.seay, '*', color='r')
        self.ax2.plot(self.seax, self.cy, '^', color='b')

        plt.savefig('fig.png')
        self.graph.setPixmap(QPixmap('fig.png'))


if __name__ =='__main__':
    app = QApplication(argv)
    m = mas2()
    app.exec_()