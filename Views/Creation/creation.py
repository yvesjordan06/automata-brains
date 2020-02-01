# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/creation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore

from Models.Automate import Automate
from Views.Creation.makeView import *

class CreationView(object):
    def __init__(self, automate:Automate, list:dict):
        self.automate = automate
        self.list = list
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(115, 125)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QScrollArea(Form)
        self.groupBox.setWidgetResizable(True)
        self.groupBox.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_2")

        #self.groupBox = QtWidgets.QGroupBox(Form)
        #self.groupBox.setObjectName("groupBox")
        self.createBtn= AutomataSelectWindow(self.automate, self.list)


        self.verticalLayout_3.addWidget(AddAlphabetWindow(self.automate))
        self.verticalLayout_3.addWidget(AddEtatWindow(self.automate))
        self.verticalLayout_3.addWidget(AddTransitionWindow(self.automate))
        self.verticalLayout_3.addWidget(self.createBtn)
        #self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Creation"))
        #self.groupBox.setTitle(_translate("Form", "Creation"))
        #self.createBtn.setText(_translate("GroupBox", "Creer l'automate"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CreationView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
