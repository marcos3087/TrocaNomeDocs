# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fmain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_principal(object):
    def setupUi(self, principal):
        if not principal.objectName():
            principal.setObjectName(u"principal")
        principal.setWindowModality(Qt.ApplicationModal)
        principal.resize(505, 603)
        self.mnuSair = QAction(principal)
        self.mnuSair.setObjectName(u"mnuSair")
        self.mnuSair.setCheckable(False)
        self.mnuSair.setChecked(False)
        self.mnuCadPh = QAction(principal)
        self.mnuCadPh.setObjectName(u"mnuCadPh")
        self.mnuCadMO = QAction(principal)
        self.mnuCadMO.setObjectName(u"mnuCadMO")
        self.mnuCadParametros = QAction(principal)
        self.mnuCadParametros.setObjectName(u"mnuCadParametros")
        self.mnuExportaResultado = QAction(principal)
        self.mnuExportaResultado.setObjectName(u"mnuExportaResultado")
        self.mnuAnaSolocitacaoSolo = QAction(principal)
        self.mnuAnaSolocitacaoSolo.setObjectName(u"mnuAnaSolocitacaoSolo")
        self.mnuAnaResultadoSolo = QAction(principal)
        self.mnuAnaResultadoSolo.setObjectName(u"mnuAnaResultadoSolo")
        self.mnuAnaImpResultadoSolo = QAction(principal)
        self.mnuAnaImpResultadoSolo.setObjectName(u"mnuAnaImpResultadoSolo")
        self.mnuAnaCalcFatoresSolo = QAction(principal)
        self.mnuAnaCalcFatoresSolo.setObjectName(u"mnuAnaCalcFatoresSolo")
        self.mnuAnaPesqSolo = QAction(principal)
        self.mnuAnaPesqSolo.setObjectName(u"mnuAnaPesqSolo")
        self.mnuAnaAlteraProtSolo = QAction(principal)
        self.mnuAnaAlteraProtSolo.setObjectName(u"mnuAnaAlteraProtSolo")
        self.mnuAnaSolicitacaoFolha = QAction(principal)
        self.mnuAnaSolicitacaoFolha.setObjectName(u"mnuAnaSolicitacaoFolha")
        self.mnuAnaResultadoFolha = QAction(principal)
        self.mnuAnaResultadoFolha.setObjectName(u"mnuAnaResultadoFolha")
        self.mnuAnaImprResultadoFolha = QAction(principal)
        self.mnuAnaImprResultadoFolha.setObjectName(u"mnuAnaImprResultadoFolha")
        self.mnuAnaCalcFatoresFolha = QAction(principal)
        self.mnuAnaCalcFatoresFolha.setObjectName(u"mnuAnaCalcFatoresFolha")
        self.mnuAnaPesqFolha = QAction(principal)
        self.mnuAnaPesqFolha.setObjectName(u"mnuAnaPesqFolha")
        self.mnuAnaAlteraProtFolha = QAction(principal)
        self.mnuAnaAlteraProtFolha.setObjectName(u"mnuAnaAlteraProtFolha")
        self.mnuAnaSolicitacaoTextura = QAction(principal)
        self.mnuAnaSolicitacaoTextura.setObjectName(u"mnuAnaSolicitacaoTextura")
        self.mnuAnaResultadoTextura = QAction(principal)
        self.mnuAnaResultadoTextura.setObjectName(u"mnuAnaResultadoTextura")
        self.mnuAnaImpResultadoTextura = QAction(principal)
        self.mnuAnaImpResultadoTextura.setObjectName(u"mnuAnaImpResultadoTextura")
        self.mnuAnaPesqTextura = QAction(principal)
        self.mnuAnaPesqTextura.setObjectName(u"mnuAnaPesqTextura")
        self.mnuAnaAlteraProtTextura = QAction(principal)
        self.mnuAnaAlteraProtTextura.setObjectName(u"mnuAnaAlteraProtTextura")
        self.mnuRelAnaSolos = QAction(principal)
        self.mnuRelAnaSolos.setObjectName(u"mnuRelAnaSolos")
        self.mnuPlanilhaSolosCom = QAction(principal)
        self.mnuPlanilhaSolosCom.setObjectName(u"mnuPlanilhaSolosCom")
        self.mnuPlanilhaSolosParcial = QAction(principal)
        self.mnuPlanilhaSolosParcial.setObjectName(u"mnuPlanilhaSolosParcial")
        self.mnuRelEntregaSolos = QAction(principal)
        self.mnuRelEntregaSolos.setObjectName(u"mnuRelEntregaSolos")
        self.mnuPlanilhaSolos = QAction(principal)
        self.mnuPlanilhaSolos.setObjectName(u"mnuPlanilhaSolos")
        self.mnuExtratoAnaFolha = QAction(principal)
        self.mnuExtratoAnaFolha.setObjectName(u"mnuExtratoAnaFolha")
        self.mnuPlanilhaFolhaCom = QAction(principal)
        self.mnuPlanilhaFolhaCom.setObjectName(u"mnuPlanilhaFolhaCom")
        self.mnuRelEntregaFolha = QAction(principal)
        self.mnuRelEntregaFolha.setObjectName(u"mnuRelEntregaFolha")
        self.mnuEtiqueta = QAction(principal)
        self.mnuEtiqueta.setObjectName(u"mnuEtiqueta")
        self.mnuPermissoesAcesso = QAction(principal)
        self.mnuPermissoesAcesso.setObjectName(u"mnuPermissoesAcesso")
        self.mnuSobre = QAction(principal)
        self.mnuSobre.setObjectName(u"mnuSobre")
        self.mnuCadAbsorbancia = QAction(principal)
        self.mnuCadAbsorbancia.setObjectName(u"mnuCadAbsorbancia")
        self.mnuCadRemetentes = QAction(principal)
        self.mnuCadRemetentes.setObjectName(u"mnuCadRemetentes")
        self.mnuAnaLiberaSolo = QAction(principal)
        self.mnuAnaLiberaSolo.setObjectName(u"mnuAnaLiberaSolo")
        self.mnuAnaLiberaFolha = QAction(principal)
        self.mnuAnaLiberaFolha.setObjectName(u"mnuAnaLiberaFolha")
        self.mnuAnaLiberaTextura = QAction(principal)
        self.mnuAnaLiberaTextura.setObjectName(u"mnuAnaLiberaTextura")
        self.mnuFechamentoAnaSol = QAction(principal)
        self.mnuFechamentoAnaSol.setObjectName(u"mnuFechamentoAnaSol")
        self.mnuConfiguracao = QAction(principal)
        self.mnuConfiguracao.setObjectName(u"mnuConfiguracao")
        self.centralwidget = QWidget(principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 471, 51))
        self.groupBox.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.txtCamArq = QLineEdit(self.groupBox)
        self.txtCamArq.setObjectName(u"txtCamArq")
        self.txtCamArq.setGeometry(QRect(10, 20, 411, 20))
        self.btSelCam = QPushButton(self.groupBox)
        self.btSelCam.setObjectName(u"btSelCam")
        self.btSelCam.setGeometry(QRect(430, 20, 31, 23))
        icon = QIcon()
        icon.addFile(u"Imagens/diretorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btSelCam.setIcon(icon)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 100, 111, 16))
        self.lstEncontrado = QListWidget(self.centralwidget)
        self.lstEncontrado.setObjectName(u"lstEncontrado")
        self.lstEncontrado.setGeometry(QRect(20, 120, 201, 401))
        self.lstResultados = QListWidget(self.centralwidget)
        self.lstResultados.setObjectName(u"lstResultados")
        self.lstResultados.setGeometry(QRect(280, 120, 211, 401))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 100, 111, 16))
        self.btTrocaNome = QPushButton(self.centralwidget)
        self.btTrocaNome.setObjectName(u"btTrocaNome")
        self.btTrocaNome.setGeometry(QRect(210, 530, 81, 23))
        self.btConfig = QPushButton(self.centralwidget)
        self.btConfig.setObjectName(u"btConfig")
        self.btConfig.setGeometry(QRect(460, 10, 31, 23))
        icon1 = QIcon()
        icon1.addFile(u"Imagens/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btConfig.setIcon(icon1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 520, 31, 16))
        self.lblTotalEncontrado = QLabel(self.centralwidget)
        self.lblTotalEncontrado.setObjectName(u"lblTotalEncontrado")
        self.lblTotalEncontrado.setGeometry(QRect(50, 520, 121, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 520, 71, 16))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 540, 71, 20))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblTotalAlterado = QLabel(self.centralwidget)
        self.lblTotalAlterado.setObjectName(u"lblTotalAlterado")
        self.lblTotalAlterado.setGeometry(QRect(400, 520, 71, 16))
        self.lblTotalErro = QLabel(self.centralwidget)
        self.lblTotalErro.setObjectName(u"lblTotalErro")
        self.lblTotalErro.setGeometry(QRect(400, 540, 71, 16))
        self.rbCupom = QRadioButton(self.centralwidget)
        self.rbCupom.setObjectName(u"rbCupom")
        self.rbCupom.setGeometry(QRect(30, 10, 82, 17))
        self.rbCupom.setChecked(True)
        self.rbNf = QRadioButton(self.centralwidget)
        self.rbNf.setObjectName(u"rbNf")
        self.rbNf.setGeometry(QRect(130, 10, 82, 17))
        principal.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(principal)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 505, 21))
        self.mnuArquivo = QMenu(self.menuBar)
        self.mnuArquivo.setObjectName(u"mnuArquivo")
        principal.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(principal)
        self.statusBar.setObjectName(u"statusBar")
        principal.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.mnuArquivo.menuAction())
        self.mnuArquivo.addSeparator()
        self.mnuArquivo.addAction(self.mnuConfiguracao)
        self.mnuArquivo.addAction(self.mnuSair)

        self.retranslateUi(principal)

        QMetaObject.connectSlotsByName(principal)
    # setupUi

    def retranslateUi(self, principal):
        principal.setWindowTitle(QCoreApplication.translate("principal", u"Altera nome de cupom Fiscal", None))
        self.mnuSair.setText(QCoreApplication.translate("principal", u"Sair", None))
        self.mnuCadPh.setText(QCoreApplication.translate("principal", u"PH", None))
        self.mnuCadMO.setText(QCoreApplication.translate("principal", u"M.O.", None))
        self.mnuCadParametros.setText(QCoreApplication.translate("principal", u"Par\u00e2metros", None))
        self.mnuExportaResultado.setText(QCoreApplication.translate("principal", u"Exporta\u00e7\u00e3o de resultados", None))
        self.mnuAnaSolocitacaoSolo.setText(QCoreApplication.translate("principal", u"Solicita\u00e7\u00e3o de an\u00e1lise", None))
        self.mnuAnaResultadoSolo.setText(QCoreApplication.translate("principal", u"Resultado de an\u00e1lise", None))
        self.mnuAnaImpResultadoSolo.setText(QCoreApplication.translate("principal", u"Impress\u00e3o de resultado", None))
        self.mnuAnaCalcFatoresSolo.setText(QCoreApplication.translate("principal", u"C\u00e1lculo de fatores", None))
        self.mnuAnaPesqSolo.setText(QCoreApplication.translate("principal", u"Pesquisa de An\u00e1lises", None))
        self.mnuAnaAlteraProtSolo.setText(QCoreApplication.translate("principal", u"Altera\u00e7\u00e3o de cadastro de protocolo", None))
        self.mnuAnaSolicitacaoFolha.setText(QCoreApplication.translate("principal", u"Solicita\u00e7\u00e3o de an\u00e1lise", None))
        self.mnuAnaResultadoFolha.setText(QCoreApplication.translate("principal", u"Resultado de an\u00e1lise", None))
        self.mnuAnaImprResultadoFolha.setText(QCoreApplication.translate("principal", u"Impress\u00e3o de resultado", None))
        self.mnuAnaCalcFatoresFolha.setText(QCoreApplication.translate("principal", u"C\u00e1culo dos fatores", None))
        self.mnuAnaPesqFolha.setText(QCoreApplication.translate("principal", u"Pesquisa de an\u00e1lises", None))
        self.mnuAnaAlteraProtFolha.setText(QCoreApplication.translate("principal", u"Altera\u00e7\u00e3o de cadastro de protocolos", None))
        self.mnuAnaSolicitacaoTextura.setText(QCoreApplication.translate("principal", u"Solicita\u00e7\u00e3o de an\u00e1lise", None))
        self.mnuAnaResultadoTextura.setText(QCoreApplication.translate("principal", u"Resultado de an\u00e1lise", None))
        self.mnuAnaImpResultadoTextura.setText(QCoreApplication.translate("principal", u"Impress\u00e3o de resultado", None))
        self.mnuAnaPesqTextura.setText(QCoreApplication.translate("principal", u"Pesquisa an\u00e1lise", None))
        self.mnuAnaAlteraProtTextura.setText(QCoreApplication.translate("principal", u"Altera\u00e7\u00e3o de cadastro de protocolos", None))
        self.mnuRelAnaSolos.setText(QCoreApplication.translate("principal", u"Extrato de an\u00e1lise de solos", None))
        self.mnuPlanilhaSolosCom.setText(QCoreApplication.translate("principal", u"Planilha de leitura - Completa", None))
        self.mnuPlanilhaSolosParcial.setText(QCoreApplication.translate("principal", u"Planilha de leitura - Parcial", None))
        self.mnuRelEntregaSolos.setText(QCoreApplication.translate("principal", u"Entrega de Resultados", None))
        self.mnuPlanilhaSolos.setText(QCoreApplication.translate("principal", u"Planilha de leitura", None))
        self.mnuExtratoAnaFolha.setText(QCoreApplication.translate("principal", u"Extrato de an\u00e1lise de folhas", None))
        self.mnuPlanilhaFolhaCom.setText(QCoreApplication.translate("principal", u"Planilha de leitura de folhas", None))
        self.mnuRelEntregaFolha.setText(QCoreApplication.translate("principal", u"Entrega de resultados", None))
        self.mnuEtiqueta.setText(QCoreApplication.translate("principal", u"Etiqueta", None))
        self.mnuPermissoesAcesso.setText(QCoreApplication.translate("principal", u"Permiss\u00e3o de acesso", None))
        self.mnuSobre.setText(QCoreApplication.translate("principal", u"Sobre", None))
        self.mnuCadAbsorbancia.setText(QCoreApplication.translate("principal", u"Abserob\u00e2ncia", None))
        self.mnuCadRemetentes.setText(QCoreApplication.translate("principal", u"Remetentes", None))
        self.mnuAnaLiberaSolo.setText(QCoreApplication.translate("principal", u"Liberar an\u00e1lises", None))
        self.mnuAnaLiberaFolha.setText(QCoreApplication.translate("principal", u"Liberar an\u00e1lises", None))
        self.mnuAnaLiberaTextura.setText(QCoreApplication.translate("principal", u"Liberar an\u00e1lises", None))
        self.mnuFechamentoAnaSol.setText(QCoreApplication.translate("principal", u"Fechamento de an\u00e1lises (C\u00e1culo de bases)", None))
        self.mnuConfiguracao.setText(QCoreApplication.translate("principal", u"Configura\u00e7\u00e3o", None))
        self.groupBox.setTitle(QCoreApplication.translate("principal", u"Local dos arquivos", None))
        self.btSelCam.setText("")
        self.label.setText(QCoreApplication.translate("principal", u"Arquivos Encontrados", None))
        self.label_2.setText(QCoreApplication.translate("principal", u"Resultados", None))
        self.btTrocaNome.setText(QCoreApplication.translate("principal", u"Trocar nomes", None))
#if QT_CONFIG(tooltip)
        self.btConfig.setToolTip(QCoreApplication.translate("principal", u"Configura\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.btConfig.setText("")
        self.label_3.setText(QCoreApplication.translate("principal", u"Total:", None))
        self.lblTotalEncontrado.setText(QCoreApplication.translate("principal", u"0", None))
        self.label_4.setText(QCoreApplication.translate("principal", u"Total alterado:", None))
        self.label_5.setText(QCoreApplication.translate("principal", u"Total erro:", None))
        self.lblTotalAlterado.setText(QCoreApplication.translate("principal", u"0", None))
        self.lblTotalErro.setText(QCoreApplication.translate("principal", u"0", None))
        self.rbCupom.setText(QCoreApplication.translate("principal", u"Cupom Fiscal", None))
        self.rbNf.setText(QCoreApplication.translate("principal", u"Nota Fiscal", None))
        self.mnuArquivo.setTitle(QCoreApplication.translate("principal", u"Arquivo", None))
    # retranslateUi
