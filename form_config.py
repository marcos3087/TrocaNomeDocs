import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog,QListWidgetItem,QMessageBox
from fconfig import Ui_config
'''
Tela que permite a manipulação de valores dentro do arquivo conf.ini

Inicialmente o arquivo precisa somente do caminho onde se encontra instalado o Tesseract.exe.

Localiza a pasta e salva na variável correspondente dentro do arquivo de configuração o valor na tela.
'''

class form_config(QMainWindow, Ui_config): 
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.initComponents()
        self.carregaConfig()

    def initComponents(self):
        self.btPesqCamTess.clicked.connect(self.PesqCamTess)
        self.btGravar.clicked.connect(self.gravar)
        self.carregaConfig()


    def PesqCamTess(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenamedir= QFileDialog.getExistingDirectory(self, "Selecionar Diretório",
                                                "",
                                                QFileDialog.ShowDirsOnly)
        self.txtCamTess.setText(filenamedir)

    def gravar(self):
        f = open("conf.ini","r")
        linhas = f.readlines()
        with open("conf.ini",'w') as f:
            for i, linha in enumerate(linhas,1):
                if(linha[0] != ";"  and len(linha)>3):
                    aux = linha.split("=")
                    nomvar = aux[0].strip()
                    valor = self.capturaTela(nomvar)
                    newlinha = nomvar + " = " + valor +"\n"
                    f.writelines(newlinha)
                else:
                    f.writelines(linha)

            f.close()

        
        QMessageBox.about(self, "ATENÇÃO","Dados gravados")
        return


    def carregaConfig(self):
        fl = open("conf.ini")
        leu = fl.readlines()
        for linha in leu:
            if linha[0] != ";" and len(linha)>3:
                aux = linha.split("=")
                nomvar = aux[0].strip()
                valor = r""+aux[1].strip()
                self.aplicaTela(nomvar,valor)
        fl.close()

    def aplicaTela(self,nomvar,valor):
        if(nomvar == "camtess"):
            self.txtCamTess.setText(valor)
        if(nomvar == "marcadorpadrao"):
            if(valor =="cupom"):
                self.cbTipoDocumento.setCurrentIndex(0)
            else:
                self.cbTipoDocumento.setCurrentIndex(1)

    def capturaTela(self,nomvar):
        retorno = ""
        if(nomvar == "camtess"):
            retorno = r""+ self.txtCamTess.text()
        if(nomvar == "marcadorpadrao"):
            if(self.cbTipoDocumento.currentIndex() == 0):
                retorno="cupom"
            else:
                retorno= "nota"
        
        return retorno