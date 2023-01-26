# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fconfig.ui'
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
        config.resize(403, 179)
        self.btPesqCamTess = QPushButton(config)
        self.btPesqCamTess.setObjectName(u"btPesqCamTess")
        self.btPesqCamTess.setGeometry(QRect(360, 40, 25, 20))
        icon = QIcon()
        icon.addFile(u"Imagens/diretorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btPesqCamTess.setIcon(icon)
        self.btGravar = QPushButton(config)
        self.btGravar.setObjectName(u"btGravar")
        self.btGravar.setGeometry(QRect(150, 140, 75, 23))
        self.txtCamTess = QLineEdit(config)
        self.txtCamTess.setObjectName(u"txtCamTess")
        self.txtCamTess.setGeometry(QRect(20, 40, 341, 20))
        self.label = QLabel(config)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 16))
        self.label_2 = QLabel(config)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 191, 16))
        self.line = QFrame(config)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 411, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.cbTipoDocumento = QComboBox(config)
        self.cbTipoDocumento.addItem("")
        self.cbTipoDocumento.addItem("")
        self.cbTipoDocumento.setObjectName(u"cbTipoDocumento")
        self.cbTipoDocumento.setGeometry(QRect(20, 90, 341, 22))
        self.line_2 = QFrame(config)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 110, 401, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(config)

        QMetaObject.connectSlotsByName(config)
    # setupUi

    def retranslateUi(self, config):
        config.setWindowTitle(QCoreApplication.translate("config", u"Configura\u00e7\u00f5es", None))
        self.btPesqCamTess.setText("")
        self.btGravar.setText(QCoreApplication.translate("config", u"Gravar", None))
        self.label.setText(QCoreApplication.translate("config", u"Caminho Tesseract", None))
        self.label_2.setText(QCoreApplication.translate("config", u"Marcador Padr\u00e3o tipo de documento", None))
        self.cbTipoDocumento.setItemText(0, QCoreApplication.translate("config", u"Cupom", None))
        self.cbTipoDocumento.setItemText(1, QCoreApplication.translate("config", u"Nota Fiscal", None))

    # retranslateUi

