# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/alphabet.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Alphabet import Alphabet
from Models.Automate import Automate


class Ui_Form(object):
    def __init__(self, automate:Automate):
        self.automate = automate
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(216, 172)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setStyleSheet("padding:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # Button binding
        self.pushButton.clicked.connect(lambda:self.action_ajouter_symbole())

        # Line Edit on submit Binding
        self.lineEdit.returnPressed.connect(lambda:self.action_ajouter_symbole())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Alphabet"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Inserer le symbol"))
        self.pushButton.setText(_translate("Form", "Inserer"))

    def action_ajouter_symbole(self):
        symbole = self.lineEdit.text()

        if symbole:
            self.lineEdit.clear()
            self.automate.ajouter_symbole(symbole)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
