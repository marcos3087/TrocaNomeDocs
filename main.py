import sys, os, fitz,cv2
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog,QListWidgetItem,QMessageBox
from fmain import Ui_principal
from pytesseract import pytesseract 
from PIL import Image

'''
    Projeto Python para alteração de nome de arquivos pdf com imagens de cupons fiscais, para fins de armazenamento
    do cupom ou danfe modelo 55 digitalizado.

    Fluxo:
        - Informa a pasta de origem dos arquivos pdf contendo a imagem do documento.
        - Abre o arquivo pdf
        - extrai a imagem do arquivo
        - salva um arquivo jpg auxiliar para leitura do texto
        - lê o texto do jpg do cupom ou nota fiscal tipo danfe modelo 55.
        - extrai o numero do cupom, localizando o conforme um padrão pré definido fixamente no código fonte.
            * conforme esse padrão, o código quebra o texto extraído em dois, a partir do texto fixado no fonte.
        - usando o comando CMD MOVE, move o arquivo para mesma pasta, alterando o nome do arquivo para o numero do cupom localizado.
            ex: arquivo_cupom_1.pdf é alterado para 123456.pdf (123456 número do cupom dentro do PDF) 
                exibe na tela a alteração no formato: nome_antigo.pdf - nome_novo.pf (arquivo_cupom_1.pdf - 123456.pdf)
            * caso não localize o numero ou aconteça algum erro a tentativa de renomear o arquivo apresenta a palavra erro, para que o usuario
              consiga visualizar quantos e quais arquivos não foram modificados.
            ex: arquivo_cupom_2.pdf - ERRO
    
    para que funcione como se planejou, espera-se que alguns itens sejam pré-definidos externamente ao sistema.
        1 - O arquivo seja pdf e contenha somente a imagem do cupom
        2 - seja um cupom por arquivo
        3 - o texto para localizar o numero do cupom seja [NFC-e numero] ou [NFC-e n°] (isso foi definido com base no padrão do propróstio do desenvolvimento do sistema,
                                                                                        que era alterar nomes dos cupons em uma empresa específica que tem somente esses
                                                                                        dois padrões de texto no cupom.) 
        4 - é obrigatório ter instalado na máquina que se vai rodar a aplicação o tesseract que será responsável pela abertura do pdf e extrassão do jpg
            o tesseract foi baixado no link: https://github.com/UB-Mannheim/tesseract/wiki em 25/12/2022
        5 - Foi desenvolvido para um sistema operacional WINDOWS, porém é simples de ajustar a programação para qualquer outro sistema operacional.
    
    Libs utilizadas:
        Formularios desenvolvidos em PYQT5
        fitz - (PyMuPDF) pip install pymudpdf
        PIL - Pyllow pip install pyllow


    Conclusão do projeto: 28/12/2022
    Desenvolvido por: Marcos Vilela Alves - Programador desde 2007
    
'''
class main(QMainWindow, Ui_principal): 
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.camtess = ""
        self.marcadorpadrao = "cupom"
        self.contaErro = 0
        self.contaTrocou = 0
        self.lerconf()
        self.initComponents()


    def initComponents(self):
        self.mnuSair.triggered.connect(self.Sair)
        self.mnuConfiguracao.triggered.connect(self.abreConfig)
        self.btConfig.clicked.connect(self.abreConfig)
        self.btSelCam.clicked.connect(self.SelCam)
        self.btTrocaNome.clicked.connect(self.Trocar)        
        self.txtCamArq.returnPressed.connect(self.listaArquivos)

        #Marca o radio de acordo com a configuração. padrao é cupom
        if(self.marcadorpadrao == "nota"):
            self.rbCupom.setChecked(False)
            self.rbNf.setChecked(True)
        else:
            self.rbCupom.setChecked(True)
            self.rbNf.setChecked(False)


    
    #Lê o arquivo de configuração e armazena os dados na memoria
    def lerconf(self):
        f = open("conf.ini", "r")
        linhas = f.readlines()
        for linha in linhas:
            if(linha[0]!= ";" and len(linha)>3):
                aux =  linha.split("=")
                nomvar = aux[0].strip().replace("\n","")
                valor = aux[1].strip().replace("\n","")
                self.defineValores(nomvar, valor)

    # ajusta e aplica valores encontrados na configuração 
    # nome da variavel na configuração.
    # valor que existe no arquivo
    # nomvar = valorNoArquivo.
    def defineValores(self, nomvar, valor):
        ''' Retira as / e troca por \ '''
        valor = valor.replace('/','\\')
        valor = valor.replace('\\','\##')
        valor = valor.replace('##','')


        if(nomvar == "camtess"):
            self.camtess = valor
        if(nomvar == "marcadorpadrao"):
            self.marcadorpadrao = valor

    #Ajusta a string trocando / por \
    def ajustaString(self, valor):
        aux = valor.split("/")
        val1 = ""
        i=1 
        while(i<len(aux)):
            val1 += fr"\{aux[i]}"
            i+=1
        valor = val1.replace("\#","")

        return valor

    #Abre a tela de configurações.
    def abreConfig(self):
        from form_config import form_config
        self.per = form_config()
        self.per.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.per.setEnabled(True)
        self.per.show()

    # Méotdo para trocar os nomes dos arquivos;
    def Trocar(self):

        self.lstResultados.clear()
        self.contaTrocou = 0
        self.contaErro = 0
        total = len(self.lstEncontrado)
        #Tem que localizar ao menos 1 arquivo na pasta
        if(total == 0):
            QMessageBox.warning(self, "ATENÇÃO","Nenhum arquivo para ser processado. Pesquise um diretório que possua arquivos PDF.")
            return

        i=0


        #para cada arquivo pdf localizado, abre o arquivo, retira a imagem do cupom, lê o cupom e extrai o numero
        #troca o nome do arquivo para o numeroDoCupom.pdf
        while(i< total):

            #Abre o arquivo pdf com fitz
            filenamedir = self.txtCamArq.text()
            filenamedir = filenamedir.replace("/","\\")

            nomarq = self.lstEncontrado.item(i).text()
            filename = filenamedir + "\\"+nomarq
            pdf_file = fitz.open(filename)
            page = pdf_file[0] 
            
            # o Caminho do tesseract vem do arquivo conf.ini
            path_to_tesseract = r"" + self.camtess + r"\tesseract.exe"
            if(self.rbCupom.isChecked()):
                #Percorre as imagens localizadas.
                for image_index, img in enumerate(page.get_images(), start=1): 
                
                    xref = img[0] 
                    #Extrai a imagem do pdf
                    pix = fitz.Pixmap(pdf_file,xref)
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)

                    #Salva um arquivo jpg na mesma pasta do pdf para extrair o texto
                    pix1._writeIMG(filenamedir + "\\salvou.jpg",0)

                    # caminho do tesseract, para que consiga extrair o texto da imagem
                    # o Caminho do tesseract vem do arquivo conf.ini
                    path_to_tesseract = r"" + self.camtess + r"\tesseract.exe"
                    img = Image.open(filenamedir + "\\salvou.jpg") 

                    pdf_file.close()

                    # Retira o texto da imagem
                    pytesseract.tesseract_cmd = path_to_tesseract 
                    text = pytesseract.image_to_string(img) 
                    text = text[:-1]
                    #retira todas as quebras de pagina do texto

                    text = text.replace("\n","")

                    ''' Nos moldes que o projeto foi criado, os cupons apresentaram dois formatos de texto para localizar o numero
                        no primeiro, o numero vem depois do texto NFC-e numero;
                        no segundo, o numero do cumpom vem depois de NFC-e n°
                        Isso pode variar no sistema emissor do cupom.
                        basta ajustar os padrões.
                    '''
                    if(text.find("NFC-e numero") != -1 or text.find("NFC-e n°") != -1):
                        #Captura o numero do cupom
                        if(text.find("NFC-e n°") !=-1):
                            numcupom = self.capturaNumero("NFC-e n°",text)
                        else:
                            numcupom = self.capturaNumero("NFC-e numero",text)

                        # se conseguiu localizar o numero    
                        if(numcupom != ""):
                            #convert para inteiro, para retirar zeros a esquerda
                            intnumcupom = int(numcupom)
                            #volta para string para concatenar na string de troca de nome de arquivo.
                            numcupom = str(intnumcupom)

                            #Pega o nome da pasta de origem do arquivo e monta a stirng para localizar o arquivo via cmd
                            pastanom = self.txtCamArq.text()
                            arquori =  str(pastanom + "/" + nomarq)
                            arquori = self.ajustaString(arquori)


                            arquori = arquori.replace('/','\\')
                            arquori = arquori.replace('\\','\##')
                            arquori = arquori.replace('##','')

                            #Monta a string para arquivo de destino com o novo nome composto pelo numero do cupom
                            arqudes = pastanom+"/"+numcupom+".pdf"
                            arqudes = arqudes.replace("/","\##")
                            #arqudes = arqudes.replace("\\","\##")
                            arqudes = arqudes.replace("##","")

                            #monta o comando CMD
                            xcopy = r'MOVE /y  ' + arquori  +r' ' + arqudes  
                            #roda o comando CMD
                            ret = os.system(xcopy)
                            #Se retornou 0, ou seja, sucesso
                            if(ret==0):
                                # Coloca na ListWidget o arquivo modificado, informando qual o resultado
                                # ex: arquivo_cupom_1.pdf - 123456.pdf
                                txtres = nomarq + " - " + numcupom+".pdf"
                                item = QListWidgetItem(txtres)
                                self.lstResultados.addItem(item) 

                                self.contaTrocou += 1
                            else:
                                #Exibe erro e conta
                                self.gravaerro(nomarq) 
                        else:
                                #Exibe erro e conta
                            self.gravaerro(nomarq)
                    else:
                                #Exibe erro e conta
                        self.gravaerro(nomarq)
                
            else:
                ##NOTA FISCAL
                x = page.get_images()
                for image_index, img in enumerate(page.get_images(), start=1): 
                
                    xref = img[0] 
                    #Extrai a imagem do pdf
                    pix = fitz.Pixmap(pdf_file,xref)
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    

                    #Salva um arquivo jpg na mesma pasta do pdf para extrair o texto
                    pix1._writeIMG(filenamedir + "\\salvou.jpg",0)
                    
                    # caminho do tesseract, para que consiga extrair o texto da imagem
                    # o Caminho do tesseract vem do arquivo conf.ini
                    path_to_tesseract = r"" + self.camtess + r"\tesseract.exe"

                    pdf_file.close()

                    img = cv2.imread(filenamedir + "\\salvou.jpg")
                    pedaco = img[250:800,1200:4150]
                    cv2.imwrite(filenamedir + "\\salvou2.jpg",pedaco)


                    pytesseract.tesseract_cmd = path_to_tesseract 
                    
                    
                    txtnota = pytesseract.image_to_string(Image.open(filenamedir + "\\salvou2.jpg"))
                    numnota, serie = self.pesquisaNumNota(txtnota)

                    
                    if(int(numnota) != 0):
                        #Pega o nome da pasta de origem do arquivo e monta a stirng para localizar o arquivo via cmd
                            pastanom = self.txtCamArq.text()
                            arquori =  str(pastanom + "/" + nomarq)
                            arquori = self.ajustaString(arquori)


                            arquori = arquori.replace('/','\\')
                            arquori = arquori.replace('\\','\##')
                            arquori = arquori.replace('##','')

                            #Monta a string para arquivo de destino com o novo nome composto pelo numero do cupom
                            arqudes = pastanom+"/"+numnota+".pdf"
                            arqudes = arqudes.replace("/","\##")
                            #arqudes = arqudes.replace("\\","\##")
                            arqudes = arqudes.replace("##","")

                            #monta o comando CMD
                            xcopy = r'MOVE /y  ' + arquori  +r' ' + arqudes  
                            #roda o comando CMD
                            ret = os.system(xcopy)
                            #Se retornou 0, ou seja, sucesso
                            if(ret==0):
                                # Coloca na ListWidget o arquivo modificado, informando qual o resultado
                                # ex: arquivo_cupom_1.pdf - 123456.pdf
                                txtres = nomarq + " - " + numnota+".pdf"
                                item = QListWidgetItem(txtres)
                                self.lstResultados.addItem(item) 

                                self.contaTrocou += 1
                            else:
                                #Exibe erro e conta
                                self.gravaerro(nomarq) 
                    else:
                        self.gravaerro(nomarq)
                    

            i +=1

        QMessageBox.about(self, "Concluído","Processo concluído, verifique os arquivos renomeados.")
        #Mostra os totais.
        self.lblTotalAlterado.setText(str(self.contaTrocou))
        self.lblTotalErro.setText(str(self.contaErro))

    def pesquisaNumNota(self, texto):
        serie = "000"
        numnota = "000000000"
        texto = texto.replace("\n","") # tira o enter.
        if texto.find("312"):
            i = texto.index("312")
            fim = i+100
            while i<len(texto):
                
                teste = texto[i:i+50].replace(" ","")
                if(teste.isnumeric() == True):
                    chave= teste
                    if(chave[0:3]=="312"):
                        chave = chave.replace(" ","") # tira o expaco
                        numnota = int(chave[25:34])
                        serie = int(chave[22:25])
                        break
                i+=1
        return str(numnota), str(serie)

    #Métotdo para colocar a palavra erro na frente do nome original, informando assim que não houve sucesso na troca de nome
    #Ex: arquivo_cupom_2.pdf - ERRO
    def gravaerro(self, nomarq):
        txtres = nomarq + " - ERRO"
        item = QListWidgetItem(txtres)
        self.lstResultados.addItem(item)
        #Conta o erro
        self.contaErro += 1

    #Limpa o formulário, reniciando para novas execuções
    def limpa(self):
        self.lstResultados.clear()
        self.lstEncontrado.clear()
        self.lblTotalAlterado.setText("0")
        self.lblTotalEncontrado.setText("0")
        self.lblTotalErro.setText("0")
        
        self.contaErro = 0
        self.contaTrocou = 0


    '''
        Captura o numero do cupom do texto extraido do arquivo, utilizando o padrao de pesquisa passado.
        Cada sistema emissor de cupom pode ter seu padrão, e na chamada desse método, deve ser passado o padrao.
        ex: NFC-e numero 123456
        @param: textSearch String - Texto que vem logo antes do numero do cupom para que seja possível localizar.
        @param: txtcupom String - Texto extraído do cupom.
    '''
    def capturaNumero(self, textSearch, txtcupom):
        txtaux = txtcupom.split(textSearch)
        numcupom = ""
        for letra in txtaux[1]:
            if(letra != " "):
                if(letra.isnumeric()): 
                    numcupom += letra
                if(not letra.isnumeric() and letra != "\n"):
                    break

        return numcupom

    #Fecha o sistema
    def Sair(self):
        sys.exit()
    
    #Abre janela para localizar a pasta onde os arquivos serão alterados
    def SelCam(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenamedir= QFileDialog.getExistingDirectory(self, "Selecionar Diretório",
                                                "",
                                                QFileDialog.ShowDirsOnly)
        #Coloca o caminho da pasta no campo
        self.txtCamArq.setText(filenamedir)
        filenamedir = filenamedir.replace("/","\\")
        self.listaArquivos()
    
    #Percorre a pasta e coloca na tela os arquivos que serão alterados
    def listaArquivos(self):
        filenamedir = self.txtCamArq.text()
        self.lstResultados.clear()
        if(filenamedir == ""):
            self.lstEncontrado.clear()
            return

        self.lstEncontrado.clear()
        # Preenche a lista com os nomes dos arquivos.
        for diretorio, subpastas, arquivos in os.walk(filenamedir):
            for arquivo in arquivos:
                if(arquivo[-3::]== "pdf"):
                    item = QListWidgetItem(arquivo)
                    self.lstEncontrado.addItem(item) 
       

    
        self.lblTotalEncontrado.setText(str(self.lstEncontrado.count()))
            



        
#Inicia o sistema
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = main()
    novo.show()
    sys.exit(qt.exec_())


