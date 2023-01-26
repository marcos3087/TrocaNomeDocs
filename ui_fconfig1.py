# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fconfig1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_config(object):
    def setupUi(self, config):
        if not config.objectName():
            config.setObjectName(u"config")
        config.setWindowModality(Qt.WindowModal)
        config.resize(403, 129)
        self.btPesqCamTess = QPushButton(config)
        self.btPesqCamTess.setObjectName(u"btPesqCamTess")
        self.btPesqCamTess.setGeometry(QRect(360, 40, 25, 20))
        icon = QIcon()
        icon.addFile(u"lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btPesqCamTess.setIcon(icon)
        self.btGravar = QPushButton(config)
        self.btGravar.setObjectName(u"btGravar")
        self.btGravar.setGeometry(QRect(180, 80, 75, 23))
        self.txtCamTess = QLineEdit(config)
        self.txtCamTess.setObjectName(u"txtCamTess")
        self.txtCamTess.setGeometry(QRect(20, 40, 341, 20))
        self.label = QLabel(config)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 16))

        self.retranslateUi(config)

        QMetaObject.connectSlotsByName(config)
    # setupUi

    def retranslateUi(self, config):
        config.setWindowTitle(QCoreApplication.translate("config", u"Configura\u00e7\u00f5es", None))
        self.btPesqCamTess.setText("")
        self.btGravar.setText(QCoreApplication.translate("config", u"Gravar", None))
        self.label.setText(QCoreApplication.translate("config", u"Caminho Tesseract", None))
    # retranslateUi

