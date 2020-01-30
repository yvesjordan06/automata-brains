# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nom.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(231, 148)
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(GroupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        self.label.setText(_translate("GroupBox", "Nom automate"))
        self.lineEdit.setPlaceholderText(_translate("GroupBox", "A0"))
        self.pushButton.setText(_translate("GroupBox", "Modifier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupBox = QtWidgets.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()
    sys.exit(app.exec_())
