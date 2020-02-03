# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/central.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Automate import Automate
from Views.Affichage.bigReconnaisance import Ui_GroupBox as BigReconnaissanceUI
from Views.Affichage.transitionView import Ui_Form as TransitionUI
from Views.Affichage.imageViewer import QImageViewer


class SeeTransitionWindow(QtWidgets.QWidget):


    def __init__(self, automate: Automate):
        super(SeeTransitionWindow, self).__init__()

        self.ui = TransitionUI(automate)

        self.ui.setupUi(self)

class SeeBigReconnaissanceWindow(QtWidgets.QWidget):


    def __init__(self, automate: Automate):
        super(SeeBigReconnaissanceWindow, self).__init__()

        self.ui = BigReconnaissanceUI(automate)

        self.ui.setupUi(self)

    def setResult(self, text):
        self.ui.setResult(text)

class Ui_TabWidget(object):
    def __init__(self, automate):
        self.automate = automate
        self.automate.reconnaissance.connect(self.set_reconnaisance_mode)
    def setupUi(self, TabWidget):
        self.tab = TabWidget
        TabWidget.setObjectName("TabWidget")
        TabWidget.setWindowModality(QtCore.Qt.NonModal)
        TabWidget.resize(278, 400)
        TabWidget.heightForWidth(800)
        TabWidget.setStyleSheet("")

        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        TabWidget.setTabBarAutoHide(True)
        self.transitionTab = SeeTransitionWindow(self.automate)
        self.transitionTab.setObjectName("transitionTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.transitionTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        TabWidget.addTab(self.transitionTab, "")
        self.reconnaissanceTab = SeeBigReconnaissanceWindow(self.automate)
        self.reconnaissanceTab.setObjectName("reconnaissanceTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.reconnaissanceTab)
        self.verticalLayout.setObjectName("verticalLayout")


        TabWidget.addTab(self.reconnaissanceTab, "")
        self.tab_3 = QImageViewer(self.automate)
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        TabWidget.addTab(self.tab_3, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setTabText(TabWidget.indexOf(self.transitionTab), _translate("TabWidget", "Transition"))

        TabWidget.setTabText(TabWidget.indexOf(self.reconnaissanceTab), _translate("TabWidget", "Reconnaissance"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Image"))

    def set_reconnaisance_mode(self, text):
        self.tab.setCurrentIndex(1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
