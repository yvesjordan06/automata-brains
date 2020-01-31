from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog, QWidget, QHBoxLayout, QPushButton, QGroupBox, QVBoxLayout

from Models.Automate import Automate


def __init__(self):
    super().__init__()

class QImageViewer(QWidget):
    def __init__(self, test:Automate):

        super().__init__()
        self.test = test
        self.test.automate_modifier.connect(self.open)
        self.image = QLabel()
        self.image.setText('Hello')
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.image)
        self.setLayout(self.lay)
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