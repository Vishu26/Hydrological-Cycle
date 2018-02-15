from readm import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.QtWidgets import *

class me(QWidget, Ui_Form):

    def __init__(self):

        super(me, self).__init__()
        self.setupUi(self)
        self.pushButton.setDisabled(True)
        self.img = 1
        self.label.setPixmap(QPixmap('Slide01.jpg'))
        self.pushButton.clicked.connect(self.prev)
        self.pushButton_2.clicked.connect(self.forw)
        self.show()

    def forw(self):

        if self.img==13:
            self.img+=1
            self.label.setPixmap(QPixmap('Slide14.jpg'))
            self.pushButton_2.setDisabled(True)
        elif self.img==1:
            self.img += 1
            self.label.setPixmap(QPixmap('Slide02.jpg'))
            self.pushButton.setDisabled(False)
        else:
            self.img += 1
            self.label.setPixmap(QPixmap('Slide0%d.jpg' % self.img if self.img < 10 else 'Slide%d.jpg' % self.img))

    def prev(self):
        if self.img==14:
            self.img-=1
            self.label.setPixmap(QPixmap('Slide13.jpg'))
            self.pushButton_2.setDisabled(False)
        elif self.img==2:
            self.img -= 1
            self.label.setPixmap(QPixmap('Slide01.jpg'))
            self.pushButton.setDisabled(True)
        else:
            self.img -= 1
            self.label.setPixmap(QPixmap('Slide0%d.jpg' % self.img if self.img < 10 else 'Slide%d.jpg' % self.img))

if __name__=='__main__':
    app = QApplication(argv)
    m = me()
    app.exec_()