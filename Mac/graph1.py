from grap import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.QtWidgets import *
import matplotlib as mpl

mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

class mas(QWidget, Ui_Form):

    def __init__(self):

        super(mas, self).__init__()
        self.setupUi(self)
        self.step = 2
        self.seax = [1990]
        self.seay = [-20]
        self.cy = [278]
        self.conc = 278
        self.ppm.valueChanged.connect(self.se)
        self.forward.clicked.connect(self.go)
        self.time.currentIndexChanged.connect(self.t)
        self.reset.clicked.connect(self.re)
        self.expo.clicked.connect(self.exp)


        fig, self.ax1 = plt.subplots()
        self.ax1.plot(self.seax, self.seay, '*', color='r')
        self.ax1.axis([1980, 2110, -30, 100])
        self.ax1.xaxis.grid()
        self.ax1.yaxis.grid()
        self.ax1.set_facecolor('gray')
        self.ax1.set_ylabel('Relative Sea Level (mm)')
        self.ax1.yaxis.label.set_color('red')
        self.ax1.tick_params(axis='y', colors='red')

        self.ax2 = self.ax1.twinx()
        self.ax2.plot(self.seax, self.cy, '^', color='b')
        self.ax2.axis([1980, 2110, 268, 1200])
        self.ax2.xaxis.grid()
        self.ax2.set_ylabel('Concentration of Carbon Dioxide (PPM)')
        self.ax2.yaxis.label.set_color('blue')
        self.ax2.tick_params(axis='y', colors='blue')

        self.ax1.set_xlabel('Date (Year)')

        plt.savefig('fig.png')
        self.graph.setPixmap(QPixmap('fig.png'))
        self.show()

    def exp(self):
        with open('graph.txt', 'w') as f:
            f.write('Date, CO2, Sea Level\n')
            for i in range(len(self.cy)):
                f.write(str(self.seax[i])+', '+str(self.cy[i])+', '+str(self.seay[i])+'\n')
    def t(self):
        self.step = int(self.time.currentText().split()[0])
    def re(self):
        self.hide()
        self.__init__()


    def se(self):
        self.conc = self.ppm.value()
        self.val.setText(str(self.conc)+' ppm')

    def go(self):
        self.cy.append(self.conc)
        self.seax.append(self.seax[-1] + self.step)
        if self.seax[-1] >= 2110:
            self.forward.setDisabled(True)
            return
        x = np.log(self.conc/278)

        if x < 0.4:
            self.seay.append(85 * x - 20)
        elif x >= 0.4 and x <= 0.9:
            self.seay.append(14)
        else:
            self.seay.append(400 * (x ** 2) - 800 * x + 414)

        self.ax1.plot(self.seax, self.seay, '*', color='r')
        self.ax2.plot(self.seax, self.cy, '^', color='b')

        plt.savefig('fig.png')
        self.graph.setPixmap(QPixmap('fig.png'))


if __name__ =='__main__':
    app = QApplication(argv)
    m = mas()
    app.exec_()