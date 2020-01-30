# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/etat.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Alphabet import Alphabet
from Models.Automate import Automate
from Models.Etat import Etat


class Ui_Form(object):
    def __init__(self, automate:Automate):
        self.automate = automate

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 182)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setStyleSheet("padding:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxInitial = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxInitial.setStyleSheet("padding:8px")
        self.checkBoxInitial.setObjectName("checkBoxInitial")
        self.horizontalLayout.addWidget(self.checkBoxInitial)
        self.checkBoxFinal = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxFinal.setStyleSheet("padding:8px")
        self.checkBoxFinal.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBoxFinal)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Binding button

        self.pushButton.clicked.connect(lambda: self.action_ajouter_etat())

        self.lineEdit.returnPressed.connect(lambda: self.action_ajouter_etat())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Etat"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Inserer l\'etat"))
        self.checkBoxInitial.setText(_translate("Form", "Initial"))
        self.checkBoxFinal.setText(_translate("Form", "Final"))
        self.pushButton.setText(_translate("Form", "Inserer"))

    def action_ajouter_etat(self):
        valeur = self.lineEdit.text()

        self.lineEdit.clear()
        etat = Etat(valeur)

        # Ajout de l'etat
        # TODO Envoyer un etat ici quand l'erreur sera reparer
        self.automate.ajouter_etats(valeur)

        # Ajout de l'etat initial
        if self.checkBoxInitial.isChecked():
            self.automate.ajouter_initital(etat)
            self.checkBoxInitial.setChecked(False)

         # Ajout de l'etat final
        if self.checkBoxFinal.isChecked():
            self.automate.ajouter_final(etat)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
