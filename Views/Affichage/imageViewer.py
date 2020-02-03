
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5 import QtWidgets, QtCore

from Models.Automate import Automate


def __init__(self):
    super().__init__()

class QImageViewer(QtWidgets.QWidget):
    def __init__(self, test:Automate):
        super().__init__()
        self.test = test
        self.test.automate_modifier.connect(self.open)
        self.image = QtWidgets.QLabel()
        self.image.setText('Hello')
        self.groupBox = QtWidgets.QScrollArea(self)
        #self.groupBox.setMinimumWidth(300)
        self.groupBox.setWidgetResizable(True)
        self.groupBox.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addWidget(self.image)

        self.groupBox.setWidget(self.scrollAreaWidgetContents)


        self.lay = QtWidgets.QVBoxLayout(self)
        self.lay.addWidget(self.groupBox)
        #self.setLayout(self.lay)
        self.open()
    def open(self):
        path = self.test.enregistrer_image(f"{hash(self.test)}{self.test.nom}")
        print(path)
        p = QPixmap(path)
        self.image.setPixmap(p)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = QImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
    # TODO QScrollArea support mouse