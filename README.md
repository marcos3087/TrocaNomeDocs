# TrocaNomeDocs

<B>Aplicação de troca de nome de arquivos PDF</B>

Esse projeto foi desenvolvido em PYTHON para trocar o nome de arquivos de notas ficais modelo 55 (DANFE) ou cupons fiscais que foram digitalizados e salvos no formato PDF.

<B>Proposta</B><br>
Em locais onde exista grande fluxo de Notas e cupons fiscais, e que haja a necessidade de armazenar uma versão digitalizada desses documentos.

Esse módulo, analisa o arquivo PDF, reconhece o número do documento e troca o nome do arquivo para o número do documento.pdf

<B>Fluxo</B><br>
  <ul>
    <li>Informa a pasta de origem dos arquivos pdf contendo a imagem do documento.</li>
    <li>Abre o arquivo pdf</li>
    <li>extrai a imagem do arquivo</li>
    <li>salva um arquivo jpg auxiliar para leitura do texto</li>
    <li>
      Para notas fiscais
      <ol>
        <li>Recorta a imagem na região do numero da chave da nota para ler a numeração disponível no documento</li>
        <li>
          Localiza a numeração com base no inicio da chave, que no caso do projeto, era 312 sempre. Essa numeração varia de acordo com a UF onde a nota é emitida.
         </li>
         <li>Localiza o numero da nota de acordo com o padrao de chave de nota fiscal do modelo 55 (DANFE)</li>
      </ol>
     </li>
     <li> para Cupons fiscais
        <ol>
          <li> lê o texto do jpg do cupom.</li>
          <li>extrai o número do cupom, localizando-o conforme um padrão pré-definido fixamente no código fonte.
            <ol>
              <li>conforme esse padrão, o código quebra o texto extraído em dois, a partir do texto fixado no fonte.</li>
            </ol>
          </li>
        </ol>
      </li>
      <li>usando o comando CMD MOVE, move o arquivo para mesma pasta, alterando o nome do arquivo para o numero do cupom/nota localizado.<br>
     <b>ex: </b>arquivo_cupom_1.pdf é alterado para 123456.pdf (123456 número do cupom dentro do PDF) 
                exibe na tela a alteração no formato: nome_antigo.pdf - nome_novo.pf (arquivo_cupom_1.pdf - 123456.pdf)<br>
      <b>OBS:</b> caso não localize o numero ou aconteça algum erro a tentativa de renomear o arquivo apresenta a palavra erro, para que o usuario
              consiga visualizar quantos e quais arquivos não foram modificados.<br>
               <b>ex: </b>arquivo_cupom_2.pdf - ERRO
      </li>
  </ul>
  <B>Obrigatoriedades</B><br>
  Para que funcione como se planejou, espera-se que alguns itens sejam pré-definidos externamente ao sistema.
  <ol>
    <li>O arquivo seja pdf e contenha somente a imagem do cupom ou nota fiscal</li>
    <li>seja um documento por arquivo PDF</li>
    <li>o texto para localizar o numero do cupom seja [NFC-e numero] ou [NFC-e n°] (isso foi definido com base no padrão do propróstio do desenvolvimento do sistema, que era alterar nomes dos cupons em uma empresa específica que tem somente esses dois padrões de texto no cupom.) </li>
    <li>é obrigatório ter instalado na máquina que se vai rodar a aplicação o tesseract que será responsável pela abertura do pdf e extrassão do jpg o tesseract foi baixado no link: https://github.com/UB-Mannheim/tesseract/wiki em 25/12/2022</li>
    <li>Foi desenvolvido para um sistema operacional WINDOWS, porém é simples de ajustar a programação para qualquer outro sistema operacional.</li>
  
  </ol>
  <b>Libs utilizadas</b><br>
  <ul>
    <li>Formularios desenvolvidos em PYQT5</li>
    <li>fitz - (PyMuPDF) pip install pymudpdf</li>
    <li>PIL - Pyllow pip install pyllow</li>
  </ul>
