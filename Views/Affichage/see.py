# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/see.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Automate import Automate
from Views.Affichage.makeView import SeeEtatWindow, SeeTransitionWindow, SeeAlphabetWindow, ReconnaissanceWindow


class Ui_Form(object):
    def __init__(self, automate:Automate):
        self.automate = automate
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 368)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.transition = SeeTransitionWindow(self.automate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.transition.sizePolicy().hasHeightForWidth())
        self.transition.setSizePolicy(sizePolicy)

        self.transition.setObjectName("transition")
        self.verticalLayout_2.addWidget(self.transition)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alphabet = SeeAlphabetWindow(self.automate)

        self.alphabet.setObjectName("alphabet")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.alphabet)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.alphabet)
        self.etats = SeeEtatWindow(self.automate)

        self.etats.setObjectName("etats")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.etats)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addWidget(self.etats)
        self.reconnaitre = ReconnaissanceWindow()

        self.reconnaitre.setObjectName("reconnaitre")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.reconnaitre)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.reconnaitre)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", f"{self.automate.nom} (Non Determinist)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())