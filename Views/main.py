# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Views.views import SeeAutomataView, CreateAutomataView

from Models.Automate import Automate
from Models.Transition import Transition
from Models.Etat import Etat
from Models.Alphabet import Alphabet


class Ui_MainWindow(object):
    def __init__(self, automate:Automate):
        self.automate = automate
        self.automate.automate_modifier.connect(self.view_diff)
        self.liste_automate = dict()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 496)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(11)
        font.setItalic(True)
        self.frame.setFont(font)
        self.frame.setToolTipDuration(-1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newToolButton = QtWidgets.QToolButton(self.frame)
        self.newToolButton.setToolTipDuration(5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newToolButton.setIcon(icon1)
        self.newToolButton.setIconSize(QtCore.QSize(32, 32))
        self.newToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.newToolButton.setObjectName("newToolButton")
        self.horizontalLayout_3.addWidget(self.newToolButton)
        self.openToolButton = QtWidgets.QToolButton(self.frame)
        self.openToolButton.setToolTipDuration(5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openToolButton.setIcon(icon2)
        self.openToolButton.setIconSize(QtCore.QSize(32, 32))
        self.openToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.openToolButton.setObjectName("openToolButton")
        self.horizontalLayout_3.addWidget(self.openToolButton)
        self.determineToolButton = QtWidgets.QToolButton(self.frame)
        self.determineToolButton.setToolTipDuration(5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/determine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.determineToolButton.setIcon(icon3)
        self.determineToolButton.setIconSize(QtCore.QSize(32, 32))
        self.determineToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.determineToolButton.setObjectName("determineToolButton")
        self.horizontalLayout_3.addWidget(self.determineToolButton)
        self.minimizeToolButton = QtWidgets.QToolButton(self.frame)
        self.minimizeToolButton.setToolTipDuration(5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeToolButton.setIcon(icon4)
        self.minimizeToolButton.setIconSize(QtCore.QSize(32, 32))
        self.minimizeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.minimizeToolButton.setObjectName("minimizeToolButton")
        self.horizontalLayout_3.addWidget(self.minimizeToolButton)
        self.completeToolButton = QtWidgets.QToolButton(self.frame)
        self.completeToolButton.setToolTipDuration(5)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/complete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.completeToolButton.setIcon(icon5)
        self.completeToolButton.setIconSize(QtCore.QSize(32, 32))
        self.completeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.completeToolButton.setObjectName("completeToolButton")
        self.horizontalLayout_3.addWidget(self.completeToolButton)
        self.viewToolButton = QtWidgets.QToolButton(self.frame)
        self.viewToolButton.setToolTipDuration(5)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/see.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewToolButton.setIcon(icon6)
        self.viewToolButton.setIconSize(QtCore.QSize(32, 32))
        self.viewToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.viewToolButton.setObjectName("viewToolButton")
        self.horizontalLayout_3.addWidget(self.viewToolButton)
        self.unionToolButton = QtWidgets.QToolButton(self.frame)
        self.unionToolButton.setToolTipDuration(5)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unionToolButton.setIcon(icon9)
        self.unionToolButton.setIconSize(QtCore.QSize(32, 32))
        self.unionToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.unionToolButton.setObjectName("unionToolButton")
        self.horizontalLayout_3.addWidget(self.unionToolButton)



        self.infoToolButton = QtWidgets.QToolButton(self.frame)
        self.infoToolButton.setToolTipDuration(5)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoToolButton.setIcon(icon7)
        self.infoToolButton.setIconSize(QtCore.QSize(32, 32))
        self.infoToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.infoToolButton.setObjectName("infoToolButton")
        self.horizontalLayout_3.addWidget(self.infoToolButton)
        self.quitToolButton = QtWidgets.QToolButton(self.frame)
        self.quitToolButton.setToolTipDuration(5)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quitToolButton.setIcon(icon8)
        self.quitToolButton.setIconSize(QtCore.QSize(32, 32))
        self.quitToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.quitToolButton.setObjectName("quitToolButton")
        self.horizontalLayout_3.addWidget(self.quitToolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # AUTOMATA
        self.creation = CreateAutomataView(self.automate, self.liste_automate)
        self.creation.setObjectName("creation")
        self.horizontalLayout.addWidget(self.creation)

        ##CREATION
        self.automata = SeeAutomataView(self.automate)
        self.automata.setObjectName("automata")
        self.horizontalLayout.addWidget(self.automata)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 22))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuA_Propos = QtWidgets.QMenu(self.menubar)
        self.menuA_Propos.setObjectName("menuA_Propos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau = QtWidgets.QAction(MainWindow)
        self.actionNouveau.setIcon(icon2)
        self.actionNouveau.setObjectName("actionNouveau")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setIcon(icon1)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setIcon(icon8)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionDeterminiser = QtWidgets.QAction(MainWindow)
        self.actionDeterminiser.setIcon(icon3)
        self.actionDeterminiser.setObjectName("actionDeterminiser")
        self.actionMinimiser = QtWidgets.QAction(MainWindow)
        self.actionMinimiser.setIcon(icon4)
        self.actionMinimiser.setObjectName("actionMinimiser")
        self.actionVoir = QtWidgets.QAction(MainWindow)
        self.actionVoir.setIcon(icon6)
        self.actionVoir.setObjectName("actionVoir")
        self.actionCompleter = QtWidgets.QAction(MainWindow)
        self.actionCompleter.setIcon(icon5)
        self.actionCompleter.setObjectName("actionCompleter")
        self.actionNotre_Equipe = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNotre_Equipe.setIcon(icon9)
        self.actionNotre_Equipe.setObjectName("actionNotre_Equipe")
        self.actionAide = QtWidgets.QAction(MainWindow)
        self.actionAide.setIcon(icon7)
        self.actionAide.setObjectName("actionAide")
        self.actionLien_Utiles = QtWidgets.QAction(MainWindow)
        self.actionLien_Utiles.setObjectName("actionLien_Utiles")
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuActions.addAction(self.actionDeterminiser)
        self.menuActions.addAction(self.actionMinimiser)
        self.menuActions.addAction(self.actionVoir)
        self.menuActions.addAction(self.actionCompleter)
        self.menuA_Propos.addAction(self.actionNotre_Equipe)
        self.menuA_Propos.addAction(self.actionAide)
        self.menuA_Propos.addAction(self.actionLien_Utiles)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuA_Propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Binding
        self.actionVoir.triggered.connect(self.automate.visualiser)
        self.viewToolButton.clicked.connect(lambda:self.visualiser())
        self.minimizeToolButton.clicked.connect(self.minimizer)
        self.completeToolButton.clicked.connect(lambda: self.automate.copie_automate(self.automate.completer()))
        self.determineToolButton.clicked.connect(lambda: self.automate.copie_automate(self.automate.determiniser()))
        self.newToolButton.clicked.connect(lambda: self.newDialog())
        self.openToolButton.clicked.connect(lambda: self.showDialog())
        self.unionToolButton.clicked.connect(lambda: self.showUnionDialog())
        self.actionNouveau.triggered.connect(self.newDialog)
        self.actionDeterminiser.triggered.connect(lambda: self.automate.copie_automate(self.automate.determiniser()))
        self.actionCompleter.triggered.connect(lambda: self.automate.copie_automate(self.automate.completer()))
        self.actionMinimiser.triggered.connect(self.minimizer)
        self.actionOuvrir.triggered.connect(lambda: self.showDialog())

    def visualiser(self):
        self.automate.image.emit(self.automate.visualiser())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.window = MainWindow
        MainWindow.setWindowTitle(_translate("MainWindow", self.automate.nom))
        self.newToolButton.setToolTip(_translate("MainWindow", "Nouveau"))
        self.newToolButton.setStatusTip(_translate("MainWindow", "Creer un nouvel automate"))
        self.newToolButton.setText(_translate("MainWindow", "Nouveau"))
        self.openToolButton.setToolTip(_translate("MainWindow", "Ouvrir"))
        self.openToolButton.setStatusTip(_translate("MainWindow", "Ouvrir pour l\'analyse"))
        self.openToolButton.setText(_translate("MainWindow", "Ouvrir"))
        self.determineToolButton.setToolTip(_translate("MainWindow", "Determiniser"))
        self.determineToolButton.setStatusTip(_translate("MainWindow", "Determiniser l\'automata actuel"))
        self.determineToolButton.setText(_translate("MainWindow", "Derterminiser"))
        self.minimizeToolButton.setToolTip(_translate("MainWindow", "Minimizer"))
        self.minimizeToolButton.setStatusTip(_translate("MainWindow", "Minimizer l\'automate actuel"))
        self.minimizeToolButton.setText(_translate("MainWindow", "Minimiser"))
        self.completeToolButton.setToolTip(_translate("MainWindow", "Completer"))
        self.completeToolButton.setStatusTip(_translate("MainWindow", "Completer l\'automate actuelle"))
        self.completeToolButton.setText(_translate("MainWindow", "Completer"))
        self.viewToolButton.setToolTip(_translate("MainWindow", "Visualizer"))
        self.viewToolButton.setStatusTip(_translate("MainWindow", "Visualiser l\'automate"))
        self.viewToolButton.setText(_translate("MainWindow", "Visualiser"))
        self.unionToolButton.setToolTip(_translate("MainWindow", "Union"))
        self.unionToolButton.setStatusTip(_translate("MainWindow", "Fusionner 2 automates"))
        self.unionToolButton.setText(_translate("MainWindow", "Union"))



        self.infoToolButton.setToolTip(_translate("MainWindow", "Infos"))
        self.infoToolButton.setStatusTip(_translate("MainWindow", "Affiche les infos a propos de l\'automate"))
        self.infoToolButton.setText(_translate("MainWindow", "Infos"))
        self.quitToolButton.setToolTip(_translate("MainWindow", "Quitter"))
        self.quitToolButton.setStatusTip(_translate("MainWindow", "Fermer l\'application"))
        self.quitToolButton.setText(_translate("MainWindow", "Quitter"))

        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuA_Propos.setTitle(_translate("MainWindow", "A Propos"))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionDeterminiser.setText(_translate("MainWindow", "Determiniser"))
        self.actionMinimiser.setText(_translate("MainWindow", "Minimiser"))
        self.actionVoir.setText(_translate("MainWindow", "Voir"))
        self.actionCompleter.setText(_translate("MainWindow", "Completer"))
        self.actionNotre_Equipe.setText(_translate("MainWindow", "Notre Equipe"))
        self.actionAide.setText(_translate("MainWindow", "Aide"))
        self.actionLien_Utiles.setText(_translate("MainWindow", "Lien Utiles"))



    def minimizer(self):
        self.automate.copie_automate(self.automate.determiniser())

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.window,filter='*.txt',caption='Selectionnez un fichier a analyser')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                text = ' '.join(data.split('\n'))
                result = self.automate.reconnais_text(text)
                print(f'Voici le resultat {result}')
                self.automate.reconnaissance.emit(result)

    def showUnionDialog(self):
        if not self.liste_automate or len(self.liste_automate) < 2:
            self.window.setStatusTip('Aucun automate')
            return
        item, ok = QtWidgets.QInputDialog.getItem(self.window, f"Faire l'union de {self.automate.nom} avec",
                                        "Liste des automates", self.liste_automate, 0, False)

        if ok and item:
            print(f"item {item}")
            print(type(self.liste_automate[item]))
            resultat = self.automate.union_automate(self.liste_automate[item])
            resultat.definir_nom(self.automate.nom + ' U '+self.liste_automate[item].nom)
            print(f'parents {resultat.parents} Nom {[a.nom for a in resultat.parents]}')
            self.liste_automate[resultat.nom] = resultat
            self.automate.copie_automate(resultat)
            self.creation.ui.createBtn.setState()
    def newDialog(self):

        text, ok = QtWidgets.QInputDialog.getText(self.window,'Nouvel Automate','Entrez le nom')

        if ok:
            a = Automate(Alphabet([]), [], None, [], [])
            a.definir_nom(text)
            try:
                self.liste_automate[text] = a
            except:
                self.liste_automate[text+'(1)'] = a
            self.creation.ui.createBtn.setState()
            self.automate.copie_automate(a)
    def view_diff(self):
        nom = self.automate.nom
        print(f'Nom actuel {nom}')
        for x in self.liste_automate:
            print(f"Nom {x}")
            if x == nom :
                self.liste_automate[x].copie_automate(self.automate)
        print([self.liste_automate[a].etat_initial for a in self.liste_automate])

alphabet = Alphabet(['1', '2', '3'])
a = Etat('a')
b = Etat('b')
c = Etat('c')
t1 = Transition(a, '1', b)
t2 = Transition(a, '1', a)
t3 = Transition(a, '2', b)
t4 = Transition(b, '1', b)
automata = Automate(alphabet, [a, b, c], a, [a, c], [t1, t2, t3, t4])

automata.definir_nom('Brains')

def run_app(automate = automata):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(automata)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()