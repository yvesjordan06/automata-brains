# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/transition.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Automate import Automate
from Models.Etat import Etat
from Models.Transition import Transition


class Ui_Form(object):
    def __init__(self, automate: Automate):
        self.automate = automate

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 207)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.etatArriveBox = QtWidgets.QComboBox(self.groupBox)
        self.etatArriveBox.setStyleSheet("padding:8px")
        self.etatArriveBox.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.etatArriveBox)
        self.symbolBox = QtWidgets.QComboBox(self.groupBox)
        self.symbolBox.setStyleSheet("padding:8px")
        self.symbolBox.setObjectName("symbolBox")
        self.horizontalLayout_2.addWidget(self.symbolBox)
        self.etatDepartBox = QtWidgets.QComboBox(self.groupBox)
        self.etatDepartBox.setStyleSheet("padding:8px")
        self.etatDepartBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.etatDepartBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.epsilonCheck = QtWidgets.QCheckBox(self.groupBox)
        self.epsilonCheck.setStyleSheet("padding:8px")
        self.epsilonCheck.setObjectName("epsilonCheck")
        self.verticalLayout_2.addWidget(self.epsilonCheck)
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        self.etatArriveBox.setMaximumWidth(60)
        self.etatDepartBox.setMaximumWidth(60)
        self.symbolBox.setMaximumWidth(60)

        # Binding
        self.epsilonCheck.clicked.connect(self.epsilon_checker)
        self.addButton.clicked.connect(self.action_create_transition)
        self.automate.automate_modifier.connect(self.action_set_state)

        # First Set State
        self.action_set_state()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Transition"))
        self.label_2.setText(_translate("Form", "Depart"))
        self.label_3.setText(_translate("Form", "Symbol"))
        self.label.setText(_translate("Form", "Arrive"))
        self.epsilonCheck.setText(_translate("Form", "Epsilon"))
        self.addButton.setText(_translate("Form", "Ajouter"))

    def action_set_state(self):
        self.etatDepartBox.clear()
        self.symbolBox.clear()
        self.etatArriveBox.clear()
        self.etatDepartBox.addItems([str(etat) for etat in self.automate.etats])
        self.symbolBox.addItems(self.automate.alphabet.list)
        self.etatArriveBox.addItems([str(etat) for etat in self.automate.etats])

    def action_create_transition(self):
        arrive = self.etatDepartBox.currentText()
        symbole = self.symbolBox.currentText()
        depart = self.etatArriveBox.currentText()

        depart = Etat(depart)
        arrive = Etat(arrive)
        symbole = '' if self.epsilonCheck.isChecked() else symbole

        transition = Transition(depart, symbole, arrive)

        self.automate.ajoute_transition(transition)

    def epsilon_checker(self, checked: bool):
        self.symbolBox.setDisabled(checked)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
