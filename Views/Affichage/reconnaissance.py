# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/reconnaisance.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Automate import Automate
from Models.RegExp import ExpressionReguliere


class Ui_Form(object):
    def __init__(self, automate:Automate, list:dict):
        self.automate = automate
        self.list = list

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(221, 290)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultatReconnaisance = QtWidgets.QLabel(self.groupBox)
        self.resultatReconnaisance.setObjectName("resultatReconnaisance")
        self.verticalLayout_2.addWidget(self.resultatReconnaisance)
        self.lineReconnaisance = QtWidgets.QLineEdit(self.groupBox)
        self.lineReconnaisance.setStyleSheet("padding:8px")
        self.lineReconnaisance.setObjectName("lineReconnaisance")
        self.verticalLayout_2.addWidget(self.lineReconnaisance)
        self.btnReconnaitre = QtWidgets.QPushButton(self.groupBox)
        self.btnReconnaitre.setStyleSheet("padding:8px")
        self.btnReconnaitre.setObjectName("btnReconnaitre")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReconnaitre.setIcon(icon2)
        self.verticalLayout_2.addWidget(self.btnReconnaitre)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setStyleSheet("padding:8px")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setToolTipDuration(5)
        self.pushButton.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        #self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        self.lineReconnaisance.textChanged['QString'].connect(self.resultatReconnaisance.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Binding

        self.pushButton.clicked.connect(lambda: self.showDialog())
        self.btnReconnaitre.clicked.connect(self.regex)

    def retranslateUi(self, Form):
        self.window = Form
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Expression Reguliere"))
        self.resultatReconnaisance.setText(_translate("Form", "Entrez une expression reguliere"))
        self.btnReconnaitre.setText(_translate("Form", "Generer"))
        #self.groupBox_2.setTitle(_translate("Form", "Importer"))
        self.label.setText(_translate("Form", "Importer pour l'analyse"))
        self.pushButton.setToolTip(_translate("Form", "Importer"))
        self.pushButton.setStatusTip(_translate("Form", "Importer un fichier"))
        self.pushButton.setText(_translate("Form", "Ouvrir"))

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.window, filter='*.txt',
                                                      caption='Selectionnez un fichier a analyser')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                text = ' '.join(data.split('\n'))
                result = self.automate.reconnais_text(text)
                print(f'Voici le resultat {result}')
                self.automate.reconnaissance.emit(result)
    def regex(self):
        text = self.lineReconnaisance.text()



        if (text):
            nom, ok = QtWidgets.QInputDialog.getText(self.window, 'Nouvel Automate', 'Entrez le nom')

            if ok:

                result = ExpressionReguliere(text).convertir_en_afn()
                result.definir_nom(nom or text)
                self.list[nom or text] = Automate.a_partir_de(result)
                self.automate.copie_automate(Automate.a_partir_de(result))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
